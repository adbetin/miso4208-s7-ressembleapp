# Generated by Django 2.1.1 on 2018-09-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='first_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='report',
            name='resemble_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='report',
            name='second_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
