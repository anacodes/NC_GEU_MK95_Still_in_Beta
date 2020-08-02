from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from authentication.models import UserProfile
from applicants.models import JobApplied
from . import models, serializers
from .permission import IsRecruiter, IsOwner, IsSameCompany, IsActive, IsStatus
from rest_framework.parsers import MultiPartParser, FormParser
from . import code
# Create your views here.


class ShowCompanyProfileAPIView(generics.RetrieveAPIView):
    """
    API For Displaying Company Profile
    """
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ShowCompanyProfileSerializer
    queryset = models.Recruiter.objects.all()
    lookup_field = "display_name"


class RecruiterRegisterListAPIView(generics.ListCreateAPIView):
    """
    API for Recruiter Registration and List
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.RecruiterSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter, IsOwner)
    queryset = models.Recruiter.objects.all()

    def perform_create(self, serializer):
        queryset = models.Recruiter.objects.filter(user=self.request.user)
        if queryset.exists():
            raise serializers.ValidationError(
                {'error': 'Details are already present'})

        registered_recruiter = serializer.save(user=self.request.user)
        user = UserProfile.objects.get(email=self.request.user.email)
        user.is_registered = True
        user.save()
        return registered_recruiter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class RecruiterRegisterDetailAPIView(generics.RetrieveUpdateAPIView):
    """
        API for Recruiter Retrieval and Updation
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.RecruiterSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    queryset = models.Recruiter.objects.all()
    lookup_field = "user"

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class JobCreationRegisterListAPIView(generics.ListCreateAPIView):
    """
    APIs for Job Creation and Retreival for Recruiter Dashboard
    """

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobCreationSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter,
                          IsSameCompany)
    queryset = models.JobCreation.objects.all()

    def perform_create(self, serializer):
        return serializer.save(company=models.Recruiter.objects.get(
            user=self.request.user))

    def get_queryset(self):
        return self.queryset.filter(company=models.Recruiter.objects.get(
            user=self.request.user))


class JobCreationRegisterDetailListAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    """
    APIs for Job Deletion,Updation and Retreival for Recruiter Dashboard only when activate is false
    """

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobCreationSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter,
                          IsSameCompany, IsActive)
    queryset = models.JobCreation.objects.all()
    lookup_field = "jobid"

    def get_queryset(self):
        return self.queryset.filter(company=models.Recruiter.objects.get(
            user=self.request.user))


# class JobDeletionAPIView(generics.DestroyAPIView):
#     parser_classes = (MultiPartParser, FormParser)
#     serializer_class = serializers.JobCreationSerializer
#     permission_classes = (permissions.IsAuthenticated, IsRecruiter,
#                           IsSameCompany, IsStatus)
#     queryset = models.JobCreation.objects.all()
#     lookup_field = "jobid"


class JobListAPIView(generics.ListAPIView):
    """
    Job Listing for Non Authenticated User
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobListingSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = models.JobCreation.objects.filter(activate=True).filter(
        status=True)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj


class JobApplicantsAndStatusListAPIView(generics.ListAPIView):
    """
    Input job id
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobApplicantsSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    queryset = JobApplied.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def get_queryset(self):
        job_id = self.kwargs['jobid']
        return self.queryset.filter(
            job_applied_to=models.JobCreation.objects.get(jobid=job_id))


class JobApplicantsAndStatusUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    serializer_class = serializers.JobApplicantUpdateSerializer
    queryset = JobApplied.objects.all()
    lookup_field = "job_applied_id"


class ExtractJDAPIView(generics.GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    serializer_class = serializers.ExtractJobDetailsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        jd_save = models.ExtractJD.objects.create(user=self.request.user,
                                                  jd=user_data['jd'])
        # x[0].jd.url
        file_type = jd_save.jd.url.split('.')[1]
        file_path = jd_save.jd.url
        file_path = '..' + file_path
        code.extract_jd(file_type, file_path)
        models.ExtractJD.objects.filter(user=self.request.user).delete()
        return Response({"success": "OK"}, status=status.HTTP_200_OK)
