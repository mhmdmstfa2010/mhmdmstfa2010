# Generated by Django 3.2.6 on 2021-08-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextCoder', '0007_auto_20210824_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talks',
            name='duration',
            field=models.DurationField(),
        ),
    ]
