# Generated by Django 2.0.7 on 2018-10-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20181004_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='starscore',
            name='scoreDuble',
            field=models.CharField(default='', max_length=30),
        ),
    ]