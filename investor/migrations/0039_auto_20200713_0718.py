# Generated by Django 3.0.7 on 2020-07-13 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0038_auto_20200713_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role_access',
            new_name='access',
        ),
    ]