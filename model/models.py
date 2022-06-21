from django.db import models
# from django.utils.timezone import now

# class SensorType(models.Model):
#     sensor_id = models.IntegerField(primary_key=True)
#     sensor_name = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.sensor_id) + " : " + str(self.sensor_name)

class temperature(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class pressure(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class dew(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class precipitation(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class humidity(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class density(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class speed(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class direction(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()

class height(models.Model):
    reading = models.FloatField()
    time = models.DateTimeField()


# class Reading(models.Model):

#     # sensor_name = models.ForeignKey(SensorType, on_delete=models.CASCADE)

#     # date = models.DateTimeField(default=now, blank=True)
#     temperature = models.FloatField()
#     pressure = models.FloatField()
#     dew = models.FloatField()
#     precipitation = models.FloatField()
#     humidity = models.FloatField()
#     density = models.FloatField()
#     speed = models.FloatField()
#     direction = models.FloatField()
#     height = models.FloatField()
#     time = models.DateTimeField()

#     def __str__(self):
#         return "Hi"
#     # def __str__(self):
#     #     return self.sensor_type.sensor_type + " : " + str(self.time) 


