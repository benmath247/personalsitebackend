# Generated by Django 4.2 on 2023-04-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_category_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                default="https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg",
                upload_to="",
            ),
        ),
    ]
