# Generated by Django 2.2.7 on 2019-11-19 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmonCuentas', '0005_auto_20191119_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariotopseat',
            name='fotoPerfil',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/img/FotosPerfil'),
        ),
    ]