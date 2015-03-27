from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'ethogram', 'members', 'admins')

class EthogramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ethogram
        fields = ('name', 'information')

class BehaviourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Behaviour
        fields = ('name', 'information', 'ethogram')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('project', 'session_type', 'individuals')

class ObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Observation
        fields = ('session', 'recorded_behaviour', 'information',
                  'timestamp', 'individual', 'location', 'weather')

class IndividualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Individual
        fields = ('label', 'tags', 'project')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )