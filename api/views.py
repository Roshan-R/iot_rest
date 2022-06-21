from rest_framework.views import APIView
from model import models
from model import serializers

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from drf_multiple_model.views import ObjectMultipleModelAPIView
# mapping = {
#     "height" : 1,
#     "water_level" : 2,
#     "dew" : 3,
#     "precipitation" : 4,
#     "humidity" : 5,
#     "density" : 6,
#     "speed" : 7,
#     "direction" : 8,
#     "temperature" : 9,
#     "pressure" : 10,
# }

class ReadingViews(APIView):    
        """
        A view that can accept POST requests with JSON content.
        """
        parser_classes = [JSONParser]

        def post(self, request, format=None):
            time = request.data['time']

            a = models.density(reading=request.data['density'], time=time)
            a.save()
            a = models.dew(reading=request.data['dew'], time=time)
            a.save()
            a = models.direction(reading=request.data['direction'], time=time)
            a.save()
            a = models.height(reading=request.data['height'], time=time)
            a.save()
            a = models.humidity(reading=request.data['humidity'], time=time)
            a.save()
            a = models.precipitation(reading=request.data['precipitation'], time=time)
            a.save()
            a = models.pressure(reading=request.data['pressure'], time=time)
            a.save()
            a = models.speed(reading=request.data['speed'], time=time)
            a.save()
            a = models.temperature(reading=request.data['temperature'], time=time)
            a.save()

            return Response({'received data': request.data})

class MultipleView(ObjectMultipleModelAPIView):
    def get_querylist(self, *args, **kwargs):
        queryset = [
            {
                'queryset': models.density.objects.all(),
                'serializer_class': serializers.densitySerializer,
                'label': 'density',
            },
            {
                'queryset': models.dew.objects.all(),
                'serializer_class': serializers.dewSerializer,
                'label': 'dew',
            },
            {
                'queryset': models.direction.objects.all(),
                'serializer_class': serializers.directionSerializer,
                'label': 'direction',
            },
            {
                'queryset': models.height.objects.all(),
                'serializer_class': serializers.heightSerializer,
                'label': 'height',
            },
            {
                'queryset': models.humidity.objects.all(),
                'serializer_class': serializers.humiditySerializer,
                'label': 'humidity',
            },
            {
                'queryset': models.precipitation.objects.all(),
                'serializer_class': serializers.precipitationSerializer,
                'label': 'precipitation',
            },
            {
                'queryset': models.pressure.objects.all(),
                'serializer_class': serializers.pressureSerializer,
                'label': 'pressure',
            },
            {
                'queryset': models.speed.objects.all(),
                'serializer_class': serializers.speedSerializer,
                'label': 'speed',
            },
            {
                'queryset': models.temperature.objects.all(),
                'serializer_class': serializers.temperatureSerializer,
                'label': 'temperature',
            },
        ]
        return queryset

# class ReadingViews(generics.ListCreateAPIView):
#     queryset = models.Reading.objects.all()
#     serializer_class = serializers.ReadingSerializer
#     permission_classes = [IsAdminUser]
