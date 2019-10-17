# Generated by Django 2.2.6 on 2019-10-16 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0005_auto_20191016_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='dueno',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='ruta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.Ruta'),
        ),
    ]
