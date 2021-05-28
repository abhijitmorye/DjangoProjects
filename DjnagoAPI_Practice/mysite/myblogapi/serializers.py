from rest_framework import serializers
from myapp.models import UserData


class UserDataSerializer(serializers.ModelSerializer):

    profile_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = UserData
        fields = ['name', 'email_id', 'phn_number', 'profile_image']
