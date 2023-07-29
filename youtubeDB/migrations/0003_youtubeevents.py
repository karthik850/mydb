# Generated by Django 4.2.3 on 2023-07-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeDB', '0002_subscriberstories'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=1000)),
                ('eventDate', models.CharField(max_length=1000)),
                ('eventDescription', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'YoutubeEvent',
                'verbose_name_plural': 'YoutubeEvents',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
