# Generated by Django 3.2.8 on 2021-11-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurukul_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='static/images'),
        ),
    ]
