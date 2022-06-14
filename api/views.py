from rest_framework.views import APIView
from model import models
from model import serializers

from rest_framework.views import APIView
from rest_framework import generics

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

class ReadingViews(generics.ListCreateAPIView):
    queryset = models.Reading.objects.all()
    serializer_class = serializers.ReadingSerializer
    # permission_classes = [IsAdminUser]

