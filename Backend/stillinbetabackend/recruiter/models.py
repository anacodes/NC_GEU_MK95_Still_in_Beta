from django.db import models
from authentication.models import UserProfile
import hashlib
# Create your models here.


def recruiter_logo(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    encoded = hashlib.sha256(instance.user.name.replace(" ", "").encode())
    if len(encoded.hexdigest()) > 20:
        return 'recruiter/static/image/user/{0}{1}/{2}'.format(
            instance.user.id,
            encoded.hexdigest()[:20], filename)
    else:
        return 'recruiter/static/image/user/{0}{1}/{2}'.format(
            instance.user.id, encoded.hexdigest(), filename)


class Recruiter(models.Model):
    address_line1 = models.CharField(max_length=40)
    address_line2 = models.CharField(blank=True, max_length=40)
    mobile_number = models.CharField(max_length=12)
    display_name = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to=recruiter_logo, blank=True, null=True)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(to=UserProfile,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def get_full_name(self):
        """Retrieve Full Name"""
        return self.user.name

    def __str__(self):
        """Return String representation of user"""
        return self.user.name


def recruiter_jd(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    encoded = hashlib.sha256(
        instance.company.user.name.replace(" ", "").encode())
    if len(encoded.hexdigest()) > 20:
        return 'recruiter/static/jd/user/{0}{1}/{2}'.format(
            instance.company.user.id,
            encoded.hexdigest()[:20], filename)
    else:
        return 'recruiter/static/jd/user/{0}{1}/{2}'.format(
            instance.company.user.id, encoded.hexdigest(), filename)


class JobCreation(models.Model):
    jobid = models.BigAutoField(primary_key=True)
    skills = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    total_vacancy = models.PositiveIntegerField()
    salary = models.CharField(max_length=255)
    jd = models.FileField(upload_to=recruiter_jd)
    summary = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    activate = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    job_type = models.CharField(max_length=50)
    domain = models.CharField(max_length=255)
    company = models.ForeignKey(to=Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        """Job Creation Company Name"""
        return self.company.user.name


def recruiter_jd_extract(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    encoded = hashlib.sha256(instance.user.name.replace(" ", "").encode())
    if len(encoded.hexdigest()) > 20:
        return 'recruiter/static/jd/user/{0}{1}/{2}'.format(
            instance.user.id,
            encoded.hexdigest()[:20], filename)
    else:
        return 'recruiter/static/jd/user/{0}{1}/{2}'.format(
            instance.user.id, encoded.hexdigest(), filename)


class ExtractJD(models.Model):
    user = models.OneToOneField(to=UserProfile,
                                on_delete=models.CASCADE,
                                primary_key=True)
    jd = models.FileField(upload_to=recruiter_jd_extract)