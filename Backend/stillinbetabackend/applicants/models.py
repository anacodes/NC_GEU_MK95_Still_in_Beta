from django.db import models
import random
import string
from authentication.models import UserProfile
import hashlib
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    encoded = hashlib.sha256(instance.fathers_name.replace(" ", "").encode())
    if len(encoded.hexdigest()) > 20:
        return 'applicants/static/resume/user/{0}{1}/{2}'.format(
            instance.user.id,
            encoded.hexdigest()[:20], filename)
    else:
        return 'applicants/static/resume/user/{0}{1}/{2}'.format(
            instance.user.id, encoded.hexdigest(), filename)


class Applicant(models.Model):
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=40)
    address_line2 = models.CharField(blank=True, max_length=40)
    aadhar_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=255)
    highest_level_of_education = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    key_skills = models.CharField(max_length=255)
    resume = models.FileField(upload_to=user_directory_path)
    user = models.OneToOneField(to=UserProfile,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        """Return String representation of user"""
        return self.user.email


class JobApplied(models.Model):
    job_applied_id = models.BigAutoField(primary_key=True)
    applicant = models.ForeignKey(to=Applicant, on_delete=models.CASCADE)
    job_applied_to = models.ForeignKey(to=JobCreation,
                                       on_delete=models.CASCADE)
    status = models.IntegerField(default=0)