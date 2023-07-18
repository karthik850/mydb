# Generated by Django 4.2.3 on 2023-07-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'managed': True, 'verbose_name': 'Project', 'verbose_name_plural': 'Project'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectName',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='technology',
            field=models.CharField(max_length=2000),
        ),
    ]
