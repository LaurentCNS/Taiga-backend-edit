# Generated by Django 2.2.26 on 2022-11-04 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0029_auto_20221104_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstory',
            old_name='is_expired',
            new_name='is_late',
        ),
    ]
