from django.urls import path
from .views import ApplicantRegisterListAPIView, ApplicantRegisterDetailAPIView, GetActiveJobsAPIView, ApplyJobAPIView, GetActiveAppliedJobsAPIView

urlpatterns = [
    path('registration/',
         ApplicantRegisterListAPIView.as_view(),
         name='applicant_register'),
    path('registrationupdate/',
         ApplicantRegisterDetailAPIView.as_view(),
         name='applicant_register_details'),
    path('joblisting/', GetActiveJobsAPIView.as_view(),
         name='get_active_jobs'),
    path('applyjob/', ApplyJobAPIView.as_view(), name='apply_job'),
    path('dashboardapplied/',
         GetActiveAppliedJobsAPIView.as_view(),
         name='dashboard_applied'),
]
