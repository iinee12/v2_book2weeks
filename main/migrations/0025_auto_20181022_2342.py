# Generated by Django 2.0.7 on 2018-10-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20181022_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starscore',
            name='scoreComment',
            field=models.TextField(default=''),
        ),
    ]