from django.shortcuts import render, get_object_or_404
from . import models, serializers
from authentication.models import UserProfile
from .permission import IsApplicant, IsOwner
# from recruiter.models import JobCreation
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