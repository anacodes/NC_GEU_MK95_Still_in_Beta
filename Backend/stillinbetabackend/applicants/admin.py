from django.contrib import admin
from .models import Applicant, JobApplied
# Register your models here.
admin.site.register(Applicant)
admin.site.register(JobApplied)