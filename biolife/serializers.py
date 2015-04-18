from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'name', 'ethogram', 'members', 'admins', 'individuals',
                    'session_set',
                 )
        
class EthogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethogram
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'name', 'information', 'behaviours',
                 )
        
class BehaviourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behaviour
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'name', 'information', 'photo',
                 )
        


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'name', 'project', 'session_type', 'individuals', 'interval',
                    'observation_set',
                 )
        

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'session', 'recorded_behaviour', 'information', 'photo', 'timestamp', 'individual', 'location', 'weather',
                 )
        read_only_fields = ()

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'label', 'photo', 'tags',
                    'observation_set', 'project_set', 'session_set'
                 )
        read_only_fields = ('observation_set', 'project_set', 'session_set')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'name',
                 )
        

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'location',
                 )

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'weather',
                 )

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'image',
                 )

class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dummy
        fields = (
                    'id',
                    'created_by', 'updated_by', 'created_at', 'updated_at',
                    'stringProperty', 'intProperty', 'optionalStringProperty', 'dateProperty', 'imageProperty',
                    'friends'
                 )
