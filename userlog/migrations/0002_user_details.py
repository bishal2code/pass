# Generated by Django 5.0.6 on 2024-05-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('ids', models.TextField(max_length=200)),
                ('password', models.TextField(max_length=200)),
            ],
        ),
    ]
