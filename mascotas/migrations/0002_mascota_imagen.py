# Generated by Django 3.2.6 on 2021-08-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]
