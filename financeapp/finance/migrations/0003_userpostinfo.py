# Generated by Django 5.1.1 on 2025-02-24 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_months'),
        ('publicstats', '0002_alter_postcodeinfo_postcode_costliving'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=52)),
                ('postcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicstats.postcodeinfo')),
            ],
        ),
    ]
