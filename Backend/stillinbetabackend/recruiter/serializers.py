from rest_framework import serializers
from .models import Recruiter, JobCreation, ExtractJD
from authentication.models import UserProfile
from applicants.models import JobApplied, Applicant


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta():
        model = Recruiter
        fields = ('address_line1', 'address_line2', 'mobile_number',
                  'pan_number', 'website', 'logo', 'bio', 'display_name')


class JobCreationSerializer(serializers.ModelSerializer):
    class Meta():
        model = JobCreation
        fields = ('jobid', 'skills', 'email_id', 'job_title', 'location',
                  'deadline', 'total_vacancy', 'salary', 'jd', 'summary',
                  'tags', 'activate', 'status', 'job_type', 'domain')
        extra_kwargs = {
            'jobid': {
                'read_only': True
            },
            'status': {
                'default': True
            },
        }


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


class JobApplicantsApplicantSerializer(serializers.ModelSerializer):
    user = ShowCompanyProfileNameEmailSerializer()

    class Meta():
        model = Applicant
        fields = ('dob', 'gender', 'highest_level_of_education',
                  'mobile_number', 'key_skills', 'resume', 'user')


class JobApplicantsSerializer(serializers.ModelSerializer):
    applicant = JobApplicantsApplicantSerializer()

    class Meta:
        model = JobApplied
        fields = ('status', 'applicant', 'job_applied_id')

    depth = 1