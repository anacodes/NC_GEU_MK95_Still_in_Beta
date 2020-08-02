from django.urls import path
from .views import RegisterView, VerifyEmail, ResendEmail, LoginAPIView, LogoutAPIView, SetNewPassword, RequestPasswordResetEmailAPI, PasswordTokenCheckAPI

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('emailverify/', VerifyEmail.as_view(), name='email_verify'),
    path('resendemail/', ResendEmail.as_view(), name='resend_email'),
    path('requestresetemail/',
         RequestPasswordResetEmailAPI.as_view(),
         name='request_reset_email'),
    path('passwordresetcheck/<uidb64>/<token>',
         PasswordTokenCheckAPI.as_view(),
         name='password_rest_confirm'),
    path('passwordreset/', SetNewPassword.as_view(), name='password_reset'),
    path('login/', LoginAPIView.as_view(), name='login'),
    #     path('tokenrefresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('trial/', TrialApi.as_view(), name='trial'),
    path('logout/', LogoutAPIView.as_view(), name='logout')
]
