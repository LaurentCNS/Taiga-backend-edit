# Generated by Django 2.2.26 on 2022-11-23 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0031_auto_20221114_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstory',
            name='is_inProgress',
        ),
        migrations.RemoveField(
            model_name='userstory',
            name='is_noDatesTask',
        ),
        migrations.RemoveField(
            model_name='userstory',
            name='is_toCome',
        ),
    ]