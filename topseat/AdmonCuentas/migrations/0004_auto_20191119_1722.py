# Generated by Django 2.2.7 on 2019-11-19 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmonCuentas', '0003_usuariotopseat_fotoperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariotopseat',
            name='fotoPerfil',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]