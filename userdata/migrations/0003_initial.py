# Generated by Django 5.0.6 on 2024-05-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userdata', '0002_delete_user_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('email', models.TextField(max_length=200)),
                ('password', models.TextField(max_length=200)),
            ],
        ),
    ]
