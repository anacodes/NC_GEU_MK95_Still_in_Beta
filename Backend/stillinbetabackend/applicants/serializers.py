from rest_framework import serializers
from .models import Applicant, JobApplied
from recruiter.models import Recruiter, JobCreation
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


class UserProfileCompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', )


class RecruiterRegistrationDataSerializer(serializers.ModelSerializer):
    user = UserProfileCompanyNameSerializer()

    class Meta:
        model = Recruiter
        fields = ('user', 'display_name', 'website')


class JobListingSerializer(serializers.ModelSerializer):
    company = RecruiterRegistrationDataSerializer()

    class Meta:
        model = JobCreation
        fields = ('jobid', 'skills', 'email_id', 'job_title', 'location',
                  'deadline', 'total_vacancy', 'salary', 'jd', 'summary',
                  'tags', 'activate', 'status', 'company', 'job_type',
                  'domain')

        depth = 1


class JobListingAppliedSerializer(serializers.ModelSerializer):
    job_applied_to = JobListingSerializer()

    class Meta:
        model = JobApplied
        fields = ('job_applied_to', 'status')
        depth = 1


class JobApplySerializer(serializers.Serializer):
    jobid = serializers.IntegerField()
