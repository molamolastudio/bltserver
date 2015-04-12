from rest_framework import serializers
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if validated_data['password']:
            user.set_password(validated_data['password'])
            user.save()
        return instance
        
