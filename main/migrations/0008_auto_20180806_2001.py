# Generated by Django 2.0.7 on 2018-08-06 11:01

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
        ('main', '0007_reading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='id',
        ),
        migrations.AddField(
            model_name='reading',
            name='attachment_ptr',
            field=models.OneToOneField(auto_created=True, default=2, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reading',
            name='content',
            field=django_summernote.fields.SummernoteTextField(default=''),
        ),
    ]
