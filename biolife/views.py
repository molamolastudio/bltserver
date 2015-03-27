from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EthogramViewSet(viewsets.ModelViewSet):
    queryset = Ethogram.objects.all()
    serializer_class = EthogramSerializer

class BehaviourViewSet(viewsets.ModelViewSet):
    queryset = Behaviour.objects.all()
    serializer_class = BehaviourSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    