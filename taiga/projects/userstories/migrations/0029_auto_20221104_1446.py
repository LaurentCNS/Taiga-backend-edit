# Generated by Django 2.2.26 on 2022-11-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0028_expired_user_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='is_expired',
            field=models.BooleanField(blank=True, null=True, verbose_name='is expired'),
        ),
        migrations.DeleteModel(
            name='Expired',
        ),
    ]