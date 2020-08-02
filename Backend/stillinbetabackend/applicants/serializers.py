from rest_framework import serializers
from .models import Applicant, JobApplied
from authentication.models import UserProfile


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta():
        model = Applicant
        fields = ('dob', 'gender', 'address_line1', 'address_line2',
                  'aadhar_number', 'pan_number', 'fathers_name',
                  'highest_level_of_education', 'mobile_number', 'key_skills',
                  'resume')


class ApplicantSerializerUpdate(serializers.ModelSerializer):
    class Meta():
        model = Applicant
        fields = ('gender', 'address_line1', 'address_line2', 'aadhar_number',
                  'pan_number', 'highest_level_of_education', 'mobile_number',
                  'key_skills', 'resume')
