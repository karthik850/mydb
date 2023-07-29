# Generated by Django 4.2.3 on 2023-07-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeDB', '0003_youtubeevents'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubeevents',
            name='eventImage',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='myyotubevideos',
            name='thumbnail',
            field=models.URLField(default='https://drive.google.com/uc?export=view&id=143yjY3rCG_R4EWR61iOAb-XynE1ZRUFl'),
        ),
        migrations.AlterField(
            model_name='youtubeevents',
            name='eventDescription',
            field=models.TextField(),
        ),
    ]
