from django.shortcuts import render, get_object_or_404
from . import models, serializers
from authentication.models import UserProfile
from .permission import IsApplicant, IsOwner
from recruiter.models import JobCreation
# from recruiter.serializer import
import jwt
from django.conf import settings
from rest_framework import generics, status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

# Create your views here.


class ApplicantRegisterListAPIView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.ApplicantSerializer
    permission_classes = (IsApplicant, permissions.IsAuthenticated, IsOwner)
    queryset = models.Applicant.objects.all()

    def perform_create(self, serializer):
        queryset = models.Applicant.objects.filter(user=self.request.user)
        if queryset.exists():
            raise serializers.ValidationError(
                {'error': 'Details are already present'})

        registered_applicant = serializer.save(user=self.request.user)
        user = UserProfile.objects.get(email=self.request.user.email)
        user.is_registered = True
        user.save()
        return registered_applicant

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ApplicantRegisterDetailAPIView(generics.RetrieveUpdateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.ApplicantSerializerUpdate
    permission_classes = (permissions.IsAuthenticated, IsApplicant, IsOwner)
    queryset = models.Applicant.objects.all()
    lookup_field = "user"

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class GetActiveJobsAPIView(generics.ListAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobListingSerializer
    permission_classes = (permissions.IsAuthenticated, IsApplicant)
    queryset = JobCreation.objects.filter(activate=True).filter(status=True)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def get_queryset(self):
        return self.queryset.exclude(
            jobid__in=models.JobApplied.objects.filter(
                applicant__in=models.Applicant.objects.filter(
                    user=self.request.user)).values_list('job_applied_to',
                                                         flat=True))


class GetActiveAppliedJobsAPIView(generics.ListAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobListingAppliedSerializer
    permission_classes = (permissions.IsAuthenticated, IsApplicant)
    queryset = models.JobApplied.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def get_queryset(self):
        return self.queryset.filter(
            applicant__in=models.Applicant.objects.filter(
                user=self.request.user))


class ApplyJobAPIView(generics.GenericAPIView):
    serializer_class = serializers.JobApplySerializer
    permission_classes = (permissions.IsAuthenticated, IsApplicant)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_data = serializer.data
        job_details = models.JobCreation.objects.get(jobid=job_data['jobid'])
        applicant_details = models.Applicant.objects.get(
            user=self.request.user)
        obj, created = models.JobApplied.objects.get_or_create(
            applicant=applicant_details, job_applied_to=job_details)
        if not created:
            return Response({'error': 'Already Applied for this job!'},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Applied for this job successfully'},
                        status=status.HTTP_201_CREATED)
