# serializers.py
from rest_framework import serializers

from .models import Hero
from .models import echo

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class echoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = echo
        fields = ('url', 'message')
