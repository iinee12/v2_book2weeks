# Generated by Django 2.0.7 on 2018-07-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourbooks',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ourbooks',
            name='readingdate',
            field=models.CharField(max_length=14),
        ),
    ]
