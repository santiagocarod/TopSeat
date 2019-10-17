# Generated by Django 2.2.6 on 2019-10-16 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0004_auto_20191016_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=6)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='puestos_d',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='usuario',
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puestos_d', models.IntegerField(default=4)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('tarifa', models.IntegerField(default=0)),
                ('conductor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('ruta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.Ruta')),
                ('vehiculo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadPuestos', models.IntegerField(default=1)),
                ('pasajero', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('viaje', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.Viaje')),
            ],
        ),
    ]
