# Generated by Django 3.2.18 on 2023-10-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_uuid_tower_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
