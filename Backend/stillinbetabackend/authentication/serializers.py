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
