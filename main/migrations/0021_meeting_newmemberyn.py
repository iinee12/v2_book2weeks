# Generated by Django 2.0.7 on 2018-09-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_wishbooks_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='newMemberYN',
            field=models.TextField(default=''),
        ),
    ]
