from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
                    'created_by', 'updated_by',
                    'name', 'ethogram', 'members', 'admins',
                    'session_set', 'individual_set',
                 )

class EthogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethogram
        fields = (
                    'created_by', 'updated_by',
                    'name', 'information',
                    'project_set', 'behaviour_set',
                 )

class BehaviourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behaviour
        fields = (
                    'created_by', 'updated_by',
                    'name', 'ethogram', 'information', 'photo',
                    'observation_set',
                 )


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = (
                    'created_by', 'updated_by',
                    'project', 'session_type', 'individuals',
                    'observation_set',
                 )

class ObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Observation
        fields = (
                    'created_by', 'updated_by',
                    'session', 'recorded_behaviour', 'information', 'photo', 'timestamp', 'individual', 'location', 'weather'
                 )

class IndividualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Individual
        fields = (
                    'created_by', 'updated_by',
                    'label', 'photo', 'tags', 'project',
                    'observation_set',
                 )

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = (
                    'created_by', 'updated_by',
                    'name',
                    'individual_set',
                 )

