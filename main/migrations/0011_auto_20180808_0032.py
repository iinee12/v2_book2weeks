# Generated by Django 2.0.7 on 2018-08-07 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180807_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='readId',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reading',
            name='attachment_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='django_summernote.Attachment'),
        ),
    ]
