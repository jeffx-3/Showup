# Generated by Django 5.1.2 on 2024-10-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]