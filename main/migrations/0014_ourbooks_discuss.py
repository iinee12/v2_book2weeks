# Generated by Django 2.0.7 on 2018-09-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_starscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourbooks',
            name='discuss',
            field=models.TextField(default=''),
        ),
    ]