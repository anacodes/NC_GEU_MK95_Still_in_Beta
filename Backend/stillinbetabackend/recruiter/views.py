from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from authentication.models import UserProfile
from applicants.models import JobApplied, Applicant
from . import models, serializers, utils
from .permission import IsRecruiter, IsOwner, IsSameCompany, IsActive, IsStatus
from rest_framework.parsers import MultiPartParser, FormParser
from . import code
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from . import Recommendation
import pickle
scopes = ['https://www.googleapis.com/auth/calendar']
import datetime
from django_cron import CronJobBase, Schedule
# Create your views here.


class ShowCompanyProfileAPIView(generics.RetrieveAPIView):
    """
    API For Displaying Company Profile
    """
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ShowCompanyProfileSerializer
    queryset = models.Recruiter.objects.all()
    lookup_field = "display_name"


class RecruiterRegisterListAPIView(generics.ListCreateAPIView):
    """
    API for Recruiter Registration and List
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.RecruiterSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter, IsOwner)
    queryset = models.Recruiter.objects.all()

    def perform_create(self, serializer):
        queryset = models.Recruiter.objects.filter(user=self.request.user)
        if queryset.exists():
            raise serializers.ValidationError(
                {'error': 'Details are already present'})

        registered_recruiter = serializer.save(user=self.request.user)
        user = UserProfile.objects.get(email=self.request.user.email)
        user.is_registered = True
        user.save()
        return registered_recruiter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class RecruiterRegisterDetailAPIView(generics.RetrieveUpdateAPIView):
    """
        API for Recruiter Retrieval and Updation
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.RecruiterSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    queryset = models.Recruiter.objects.all()
    lookup_field = "user"

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class JobCreationRegisterListAPIView(generics.ListCreateAPIView):
    """
    APIs for Job Creation and Retreival for Recruiter Dashboard
    """

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobCreationSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter,
                          IsSameCompany)
    queryset = models.JobCreation.objects.all()

    def perform_create(self, serializer):
        return serializer.save(company=models.Recruiter.objects.get(
            user=self.request.user))

    def get_queryset(self):
        return self.queryset.filter(company=models.Recruiter.objects.get(
            user=self.request.user))


class JobCreationRegisterDetailListAPIView(
        generics.RetrieveUpdateDestroyAPIView):
    """
    APIs for Job Deletion,Updation and Retreival for Recruiter Dashboard only when activate is false
    """

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobCreationSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter,
                          IsSameCompany, IsActive)
    queryset = models.JobCreation.objects.all()
    lookup_field = "jobid"

    def get_queryset(self):
        return self.queryset.filter(company=models.Recruiter.objects.get(
            user=self.request.user))


# class JobDeletionAPIView(generics.DestroyAPIView):
#     parser_classes = (MultiPartParser, FormParser)
#     serializer_class = serializers.JobCreationSerializer
#     permission_classes = (permissions.IsAuthenticated, IsRecruiter,
#                           IsSameCompany, IsStatus)
#     queryset = models.JobCreation.objects.all()
#     lookup_field = "jobid"


class JobListAPIView(generics.ListAPIView):
    """
    Job Listing for Non Authenticated User
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobListingSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = models.JobCreation.objects.filter(activate=True).filter(
        status=True)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj


class JobApplicantsAndStatusListAPIView(generics.ListAPIView):
    """
    Input job id
    """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = serializers.JobApplicantsSerializer
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    queryset = JobApplied.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def get_queryset(self):
        job_id = self.kwargs['jobid']
        return self.queryset.filter(
            job_applied_to=models.JobCreation.objects.get(jobid=job_id))


class JobApplicantsAndStatusUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    serializer_class = serializers.JobApplicantUpdateSerializer
    queryset = JobApplied.objects.all()
    lookup_field = "job_applied_id"


class ExtractJDAPIView(generics.GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    serializer_class = serializers.ExtractJobDetailsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        jd_save = models.ExtractJD.objects.create(user=self.request.user,
                                                  jd=user_data['jd'])
        # x[0].jd.url
        file_type = jd_save.jd.url.split('.')[1]
        file_path = jd_save.jd.url[1:]
        data = code.extract_jd(file_type, file_path)
        models.ExtractJD.objects.filter(user=self.request.user).delete()
        return Response({
            "success": "OK",
            "data": data
        },
                        status=status.HTTP_200_OK)


class GoogleCalenderAuthAPIView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)

    def get(self, request):
        flow = InstalledAppFlow.from_client_secrets_file(
            "media/client_secret.json",
            scopes=scopes,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        auth = flow.authorization_url(prompt='consent')
        return Response({'gauthlink': auth}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data['credentials']
            flow = InstalledAppFlow.from_client_secrets_file(
                "media/client_secret.json",
                scopes=scopes,
                redirect_uri='urn:ietf:wg:oauth:2.0:oob')
            flow.fetch_token(code=data)
            credentials = flow.credentials
            pickle.dump(credentials, open(str(request.user.id) + ".pkl", "wb"))
            credentials = pickle.load(open(
                str(request.user.id) + ".pkl", "rb"))
            service = build("calendar", "v3", credentials=credentials)
            result = service.calendarList().list().execute()
            print(result['items'][0])
            return Response({'success': 'ok'}, status=status.HTTP_200_OK)
        except expression as identifier:
            return Response({'error': 'Google Auth Failed'},
                            status=status.HTTP_401_UNAUTHORIZED)


class GoogleCalenderSetAPIView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, IsRecruiter)
    serializer_class = serializers.GoogleDateSetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        credentials = pickle.load(open(str(request.user.id) + ".pkl", "rb"))
        timezone = 'Asia/Kolkata'
        valid_data = serializer.data
        date_time_str = valid_data['date'] + " " + valid_data['time']
        try:
            job = models.JobCreation.objects.get(jobid=valid_data['jobid'])
            start_time = datetime.datetime.strptime(date_time_str,
                                                    '%Y-%m-%d %H:%M:%S')
            end_time = start_time + datetime.timedelta(hours=1)
            event = {
                'summary':
                job.job_title,
                'location':
                'Online Interview',
                'description':
                job.summary,
                'start': {
                    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    'timeZone': timezone,
                },
                'end': {
                    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    'timeZone': timezone,
                },
                'attendees': [
                    {
                        'email': valid_data['recruiter']
                    },
                    {
                        'email': valid_data['applicant']
                    },
                ],
                'conferenceData': {
                    'createRequest': {
                        'requestId': 'its done baby',
                        'conferenceSolutionKey': {
                            'type': 'hangoutsMeet'
                        }
                    }
                },
                'reminders': {
                    'useDefault':
                    False,
                    'overrides': [
                        {
                            'method': 'email',
                            'minutes': 24 * 60
                        },
                        {
                            'method': 'popup',
                            'minutes': 10
                        },
                    ],
                },
            }
            credentials = pickle.load(open(
                str(request.user.id) + ".pkl", "rb"))
            service = build("calendar", "v3", credentials=credentials)
            result = service.calendarList().list().execute()
            calendar_id = result['items'][0]['id']
            service.events().insert(calendarId=calendar_id,
                                    body=event).execute()
            email_body = "Google Meet Scheduled at " + start_time.strftime(
                '%d/%m/%Y'
            ) + " for the Position of " + job.job_title + ". Please check your Google Calender for the Time and Date."
            data = {
                'flag': 0,
                'email_body': email_body,
                'email_subject': job.job_title + " Meeting",
                'email_id': valid_data['applicant'],
            }
            utils.Util.send_email(data)
            return Response({'success': 'ok'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'failed'},
                            status=status.HTTP_401_UNAUTHORIZED)


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS,
                        run_at_times=RUN_AT_TIMES)
    code = 'recruiter.my_cron_job'  # a unique code

    def do(self):
        job = models.JobCreation.objects.filter(activate=True).filter(
            status=True)
        applicant = Applicant.objects.all()
        app_skills = []
        job_skills = []
        for x in applicant:
            app_skills.append(x.key_skills)
        print()
        for x in job:
            print(x.job_title, end=" ")
            job_skills.append(x.skills)
        print()
        choice = Recommendation.Recommendation(app_skills, job_skills)
        print(choice)
