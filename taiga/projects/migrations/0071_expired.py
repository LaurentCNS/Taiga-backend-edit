# Generated by Django 2.2.26 on 2022-11-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0070_auto_20221010_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_expired', models.BooleanField(verbose_name='is expired')),
            ],
        ),
    ]