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
            for key, value in request.data.items():

                if key == 'density':
                    a = models.density(reading=value, time=time)
                    models.density.save(a)

                elif key == 'dew':
                    a = models.dew(reading=value, time=time)
                    models.dew.save(a)

                elif key == 'direction':
                    a = models.direction(reading=value, time=time)
                    models.direction.save(a)

                elif key == 'height':
                    a = models.height(reading=value, time=time)
                    models.height.save(a)

                elif key == 'humidity':
                    a = models.humidity(reading=value, time=time)
                    models.humidity.save(a)

                elif key == 'precipitation':
                    a = models.precipitation(reading=value, time=time)
                    models.precipitation.save(a)

                elif key == 'pressure':
                    a = models.pressure(reading=value, time=time)
                    models.pressure.save(a)

                elif key == 'speed':
                    a = models.speed(reading=value, time=time)
                    models.speed.save(a)

                elif key == 'temperature':
                    a = models.temperature(reading=value, time=time)
                    models.temperature.save(a)


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
