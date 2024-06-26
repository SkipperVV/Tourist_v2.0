# Generated by Django 5.0.3 on 2024-03-25 18:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('user', models.OneToOneField(help_text='Турист', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, verbose_name='last_name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
