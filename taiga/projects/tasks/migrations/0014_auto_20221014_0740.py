# Generated by Django 2.2.26 on 2022-10-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_auto_20200615_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_begin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date begin'),
        ),
        migrations.AddField(
            model_name='task',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date end'),
        ),
    ]