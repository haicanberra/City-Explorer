# Generated by Django 4.2.1 on 2023-06-03 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_rename_address_search_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='amenity_filters',
        ),
    ]
