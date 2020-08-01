from rest_framework import serializers
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):

    passwordverify = serializers.CharField(min_length=6,
                                           style={'input_type': 'password'},
                                           write_only=True)

    class Meta:
        model = UserProfile
        fields = ('email', 'name', 'password', 'passwordverify',
                  'is_recruiter')
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'is_recruiter': {
                'required': True
            }
        }

    def validate(self, attrs):
        password = attrs.get('password', '')
        password_match = attrs.get('passwordverify', '')
        if password != password_match:
            raise serializers.ValidationError(
                {'error': 'Passwords do not match'})

        return attrs

    def create(self, validated_data):
        """Create and return and new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'])
        user.is_recruiter = validated_data['is_recruiter']
        user.save()
        return user


class VerifyEmailSerializer(serializers.Serializer):
    token = serializers.CharField()


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255,
                                     min_length=6,
                                     write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    registered = serializers.BooleanField(read_only=True)
    is_recruiter = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('email', 'password')

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact Admin')

        if not user.is_verified:
            raise AuthenticationFailed('EmailNotVerified')

        token = user.tokens()
        return {
            "email": user.email,
            "name": user.name,
            "registered": user.is_registered,
            "is_recruiter": user.is_recruiter,
            "access": token.get('access'),
            "refresh": token.get('refresh')
        }


class RequestPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email', )


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_verify = serializers.CharField(min_length=6, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ('password', 'password_verify', 'uidb64', 'token')

    def validate(self, attrs):
        try:
            password = attrs.get('password', '')
            password_verify = attrs.get('password_verify', '')
            uidb64 = attrs.get('uidb64', '')
            token = attrs.get('token', '')
            if password != password_verify:
                raise serializers.ValidationError()
            id = force_str(urlsafe_base64_decode(uidb64))
            user = UserProfile.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed()

            user.set_password(password)
            user.save()
            return user
        except AuthenticationFailed as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        except serializers.ValidationError:
            raise serializers.ValidationError(
                {'error': 'Passwords do not match'})
        return super().validate(attrs)