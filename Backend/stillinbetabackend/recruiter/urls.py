from django.urls import path
from .views import RecruiterRegisterListAPIView, RecruiterRegisterDetailAPIView, JobCreationRegisterListAPIView, JobCreationRegisterDetailListAPIView, JobListAPIView, ShowCompanyProfileAPIView, JobApplicantsAndStatusListAPIView, JobApplicantsAndStatusUpdateAPIView, ExtractJDAPIView, GoogleCalenderAuthAPIView, GoogleCalenderSetAPIView
# , JobDeletionAPIView

urlpatterns = [
    path('registration/',
         RecruiterRegisterListAPIView.as_view(),
         name="recruiter_register"),
    path('registrationupdate/',
         RecruiterRegisterDetailAPIView.as_view(),
         name="recruiter_register_update"),
    path('jobcreate/',
         JobCreationRegisterListAPIView.as_view(),
         name="job_create"),
    path('jobcreate/<int:jobid>',
         JobCreationRegisterDetailListAPIView.as_view(),
         name="job_details"),
    #     path('jobdelete/<int:jobid>',
    #          JobDeletionAPIView.as_view(),
    #          name="job_delete"),
    path('joblisting/', JobListAPIView.as_view(), name="job_listing"),
    path('company/<display_name>',
         ShowCompanyProfileAPIView.as_view(),
         name='company_display_profile'),
    path('jobapplicant/<int:jobid>',
         JobApplicantsAndStatusListAPIView.as_view(),
         name="job_applicants"),
    path('jobapplicant/status/<int:job_applied_id>',
         JobApplicantsAndStatusUpdateAPIView.as_view(),
         name='applicant_status_update'),
    path('jobcreate/jd/', ExtractJDAPIView.as_view(), name='extract_jd'),
    path('gauth/', GoogleCalenderAuthAPIView.as_view(), name='g_cal_auth'),
    path('gdateadd/', GoogleCalenderSetAPIView.as_view(), name='g_add_date'),
]