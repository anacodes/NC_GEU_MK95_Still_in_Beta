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
