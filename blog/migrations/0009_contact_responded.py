# Generated by Django 4.2 on 2023-04-27 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='responded',
            field=models.BooleanField(default=False),
        ),
    ]
