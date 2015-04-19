from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.contrib.auth.models import User

# ViewSets define the view behavior.

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return user.joined_project_set

class EthogramViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Ethogram.objects.all()
    serializer_class = EthogramSerializer

class BehaviourViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Behaviour.objects.all()
    serializer_class = BehaviourSerializer

class SessionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ObservationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

class IndividualViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class DummyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Dummy.objects.all()
    serializer_class = DummySerializer
