# Generated by Django 2.2.26 on 2022-10-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0067_auto_20201230_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_begin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
