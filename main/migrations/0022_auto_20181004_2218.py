# Generated by Django 2.0.7 on 2018-10-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_meeting_newmemberyn'),
    ]

    operations = [
        migrations.CreateModel(
            name='readingReplys',
            fields=[
                ('replyId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('replyContent', models.TextField(default='')),
                ('replyWriter', models.CharField(max_length=30)),
                ('created', models.CharField(max_length=30)),
                ('readId', models.ForeignKey(on_delete='', to='main.Reading')),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='lastorder',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='newMemberYN',
            field=models.CharField(default='', max_length=2),
        ),
    ]