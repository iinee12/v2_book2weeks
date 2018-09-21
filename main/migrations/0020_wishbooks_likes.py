# Generated by Django 2.0.7 on 2018-09-21 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_wishbooks_imgindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishbooks',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]