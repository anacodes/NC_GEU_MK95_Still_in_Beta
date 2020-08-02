from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from authentication.models import UserProfile
from . import models, serializers
from .permission import IsRecruiter, IsOwner, IsSameCompany, IsActive, IsStatus
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


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