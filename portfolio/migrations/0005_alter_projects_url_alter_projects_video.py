# Generated by Django 4.2.3 on 2023-07-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_projects_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='url',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='video',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
