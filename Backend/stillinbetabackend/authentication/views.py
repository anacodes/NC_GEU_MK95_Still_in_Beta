from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers, models, utils
from django.conf import settings


# Create your views here.
class RegisterView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = models.UserProfile.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        token.set_exp(lifetime=datetime.timedelta(days=1))

        absurl = 'http://' + 'localhost:8080/emailverify/' + '?token=' + str(
            token)
        email_body = absurl
        data = {
            'flag': 0,
            'email_body': email_body,
            'email_subject': 'Verify your email',
            'email_id': user.email,
        }

        utils.Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)
