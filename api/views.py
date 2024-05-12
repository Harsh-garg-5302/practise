from django.shortcuts import render
from .models import Car
from .serializer import CarSerializer
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from .serializer import LoginSerializer, UserResponseSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class CarModelViewSet(viewsets.ModelViewSet):
    queryset= Car.objects.all()
    serializer_class= CarSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve instance using primary key
        self.perform_destroy(instance)  # Delete instance from database
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve instance using primary key
        serializer = self.get_serializer(instance, data=request.data)  # Deserialize data
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)  # Save updated instance
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve instance using primary key
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Deserialize data for partial update
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)  # Save updated instance
        return Response(serializer.data)


class LoginApiView(generics.GenericAPIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors})
        
        data = dict(serializer.validated_data)

        username = data.get("username")
        password = data.get("password")

        user_qs = User.objects.filter(username=username)

        if not user_qs.exists():
            return Response({"error_message": "Invalid username"})
        
        user = user_qs.first()
        
        if not check_password(password, user.password):
            return Response({"error_message": "Invalid creds"})
        
        return Response({"success_message": "Login successful", "user": UserResponseSerializer(user).data})
    
class SignupApiView(generics.GenericAPIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors})
        
        data = dict(serializer.validated_data)

        username = data.get("username")
        password = data.get("password")

        user_qs = User.objects.filter(username=username)

        if not user_qs.exists():
            return Response({"error_message": "Invalid username"})
        
        user = user_qs.first()
        
        if not check_password(password, user.password):
            return Response({"error_message": "Invalid creds"})
        
        return Response({"success_message": "Login successful", "user": UserResponseSerializer(user).data})