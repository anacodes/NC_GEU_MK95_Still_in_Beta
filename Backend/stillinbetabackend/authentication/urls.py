from django.urls import path
from .views import RegisterView, VerifyEmail, ResendEmail

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('emailverify/', VerifyEmail.as_view(), name='email_verify'),
    path('resendemail/', ResendEmail.as_view(), name='resend_email'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout')
]
