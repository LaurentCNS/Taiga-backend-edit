# Generated by Django 2.2.26 on 2022-10-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0022_auto_20221010_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='date_begin',
            field=models.DateField(blank=True, null=True, verbose_name='date begin'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='date end'),
        ),
    ]
