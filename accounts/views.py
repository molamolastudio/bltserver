from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
# Social Auth imports
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLogin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user, context=
            { 'request': request })
        return Response(serializer.data)

class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLogin):
    adapter_class = GoogleOAuth2Adapter
