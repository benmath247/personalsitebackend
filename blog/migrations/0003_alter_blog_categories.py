# Generated by Django 4.2 on 2023-04-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_blog_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="categories",
            field=models.ManyToManyField(blank=True, to="blog.category"),
        ),
    ]
