# Generated by Django 2.2.6 on 2019-10-16 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0013_auto_20191016_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='ruta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.Ruta'),
        ),
    ]
