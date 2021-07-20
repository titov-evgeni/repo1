# Generated by Django 3.2.5 on 2021-07-20 05:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=30)),
                ('user_input', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
