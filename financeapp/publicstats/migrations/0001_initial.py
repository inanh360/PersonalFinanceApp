# Generated by Django 5.1.1 on 2025-02-08 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostcodeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcName', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=2)),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('housePrice', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
