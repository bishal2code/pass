# Generated by Django 5.0.6 on 2024-05-17 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='email',
            new_name='ids',
        ),
    ]
