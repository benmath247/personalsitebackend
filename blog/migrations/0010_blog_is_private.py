# Generated by Django 4.2 on 2023-05-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_contact_responded'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_private',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
