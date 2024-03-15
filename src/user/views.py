from rest_framework import generics, permissions
from .serializers import UsernameUpdateSerializer, EmailUpdateSerializer, PasswordUpdateSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


class UsernameUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsernameUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class EmailUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = EmailUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"message": "Email has been updated", "data": response.data})


class PasswordUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"message": "Password has been updated" })