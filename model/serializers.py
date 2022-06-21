from rest_framework import serializers
from .models import *

class densitySerializer(serializers.ModelSerializer):
    class Meta:
        model = density
        fields = '__all__'

class dewSerializer(serializers.ModelSerializer):
    class Meta:
        model = dew
        fields = '__all__'

class directionSerializer(serializers.ModelSerializer):
    class Meta:
        model = direction
        fields = '__all__'

class heightSerializer(serializers.ModelSerializer):
    class Meta:
        model = height
        fields = '__all__'

class humiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = humidity
        fields = '__all__'

class precipitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = precipitation
        fields = '__all__'

class pressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = pressure
        fields = '__all__'

class speedSerializer(serializers.ModelSerializer):
    class Meta:
        model = speed
        fields = '__all__'

class temperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = '__all__'

# class SensorTypeSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=SensorType

# class ReadingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reading
#         fields = ('__all__')

    # def to_representation(self, instance):
    #     self.fields['user'] =  SensorTypeSerializer(read_only=True)
    #     ret = super(ReadingSerializer, self).to_representation(instance)
    #     ret.pop('sensor_type')
    #     ret.pop('id')
    #     return ret
