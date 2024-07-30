from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializers

user = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = RegisterSerializers
