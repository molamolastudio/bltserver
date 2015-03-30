from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from accounts.serializers import UserSerializer
# Social Auth imports
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter