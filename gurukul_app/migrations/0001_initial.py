# Generated by Django 3.2.8 on 2021-11-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
                ('image', models.ImageField(blank=True, default=None, upload_to=None)),
                ('ratings', models.FloatField()),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=250)),
            ],
        ),
    ]
