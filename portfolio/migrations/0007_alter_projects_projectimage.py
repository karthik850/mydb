# Generated by Django 4.2.3 on 2023-07-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_projects_url_alter_projects_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='projectImage',
            field=models.URLField(default='https://drive.google.com/uc?export=view&id=143yjY3rCG_R4EWR61iOAb-XynE1ZRUFl'),
        ),
    ]