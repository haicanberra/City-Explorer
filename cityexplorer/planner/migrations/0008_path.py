# Generated by Django 4.2.1 on 2023-06-06 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_marker_search_marker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paths', models.JSONField(default=list)),
            ],
        ),
    ]
