# Generated by Django 3.1.6 on 2022-06-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensortype',
            name='sensor_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
