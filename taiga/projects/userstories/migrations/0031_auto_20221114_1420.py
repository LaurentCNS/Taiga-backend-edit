# Generated by Django 2.2.26 on 2022-11-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0030_auto_20221104_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='is_inProgress',
            field=models.BooleanField(blank=True, null=True, verbose_name='in progress'),
        ),
        migrations.AddField(
            model_name='userstory',
            name='is_noDatesTask',
            field=models.BooleanField(blank=True, null=True, verbose_name='no dates task'),
        ),
        migrations.AddField(
            model_name='userstory',
            name='is_toCome',
            field=models.BooleanField(blank=True, null=True, verbose_name='to come'),
        ),
    ]
