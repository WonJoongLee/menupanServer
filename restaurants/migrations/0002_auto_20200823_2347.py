# Generated by Django 3.0.8 on 2020-08-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='downinfo',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='mainpic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='menupic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='resnumber',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='respic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='upinfo',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='xco',
            field=models.FloatField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='yco',
            field=models.FloatField(default='', max_length=20),
        ),
    ]