from rest_framework import serializers
from .models import Recruiter, JobCreation
from authentication.models import UserProfile


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