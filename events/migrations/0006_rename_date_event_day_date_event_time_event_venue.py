# Generated by Django 5.1.2 on 2024-10-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='day_date',
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
