# Generated by Django 3.2.6 on 2021-09-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextCoder', '0014_alter_talks_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talks',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
