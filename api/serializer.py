from rest_framework import serializers
from .models import Car
from django.contrib.auth.models import User

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=['id','name','year','colour','seats','type']
    # name=serializers.CharField(max_length=100)
    # year=serializers.models.IntegerField()
    # colour=serializers.CharField(max_length=100)
    # seats=serializers.IntegerField()
    # type=serializers.CharField(max_length=100)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=255, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, max_length=255, allow_null=False, allow_blank=False)

class UserResponseSerializer(serializers.ModelSerializer):

    name_initials = serializers.SerializerMethodField()

    class Meta:
        model = User
        # fields = ("__all__")
        exclude = ("password",)
    
    def get_name_initials(self, obj: User):
        if obj.first_name and obj.last_name:
            return f"{obj.first_name[0]}{obj.last_name[0]}"
        else:
            return f"{obj.first_name[0]}"