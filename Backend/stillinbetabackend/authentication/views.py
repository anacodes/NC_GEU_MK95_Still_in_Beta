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


class VerifyEmail(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.VerifyEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokendata = serializer.data
        try:
            payload = jwt.decode(tokendata['token'], settings.SECRET_KEY)
            user = models.UserProfile.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({'email': 'Email Successfully Activated'},
                            status=status.HTTP_200_OK)
        except jwt.ExpiredSignature as identifier:
            return Response({'error': 'Activation Link expired'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Invalid Token'},
                            status=status.HTTP_400_BAD_REQUEST)


class ResendEmail(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ResendEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        try:
            user = models.UserProfile.objects.get(email=user_data['email'])
            if not user.is_verified:
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

                return Response(user_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Email ID is already verified'},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Email ID not found'},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            OutstandingToken.objects.filter(
                expires_at__lte=aware_utcnow()).delete()
            # BlacklistedToken.objects.all().delete()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Logged out"},
                            status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmailAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RequestPasswordResetEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        if models.UserProfile.objects.filter(email=email).exists():
            user = models.UserProfile.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            absurl = 'http://' + 'localhost:8080/resetpassword/' + '?uidb64=' + uidb64 + '&token=' + str(
                token)
            email_body = absurl
            data = {
                'flag': 1,
                'email_body': email_body,
                'email_subject': 'Reset your password',
                'email_id': user.email,
            }
            utils.Util.send_email(data)
            return Response(
                {'success': 'We have sent a link to reset your password'},
                status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email ID does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = models.UserProfile.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {'error': 'Token is not valid, please request a new one'},
                    status=status.HTTP_401_UNAUTHORIZED)
            return Response(
                {
                    'success': True,
                    'message': 'Credentials Valid',
                    'uidb64': uidb64,
                    'token': token
                },
                status=status.HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            return Response(
                {'error': 'Token is not valid, please request a new one'},
                status=status.HTTP_401_UNAUTHORIZED)


class SetNewPassword(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                'success': True,
                'message': 'Password Reset Successfully.'
            },
            status=status.HTTP_200_OK)