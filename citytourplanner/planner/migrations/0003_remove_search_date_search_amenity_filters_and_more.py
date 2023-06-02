# Generated by Django 4.2.1 on 2023-06-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_search_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='date',
        ),
        migrations.AddField(
            model_name='search',
            name='amenity_filters',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='documented',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='tourism_filters',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
