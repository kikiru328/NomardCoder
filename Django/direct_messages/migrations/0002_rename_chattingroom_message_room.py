# Generated by Django 5.0.6 on 2024-05-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("direct_messages", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="chattingRoom",
            new_name="room",
        ),
    ]
