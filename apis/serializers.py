from rest_framework import serializers
from info import models

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Account
