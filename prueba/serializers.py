from rest_framework import serializers
from prueba.models import Prueba, Logger

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = "__all__"


class ActualizarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = ['Luz','encendido']

class LoggerSerializerComplete(serializers.ModelSerializer):
    class Meta:
        model = Logger
        fields = "__all__"

class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logger
        fields = ['luz','df','ram','wifi_ip']