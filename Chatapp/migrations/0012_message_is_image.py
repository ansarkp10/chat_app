# Generated by Django 5.1 on 2024-08-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0011_remove_message_is_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_image',
            field=models.BooleanField(default=False),
        ),
    ]
