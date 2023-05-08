from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from storages.backends.s3boto3 import S3Boto3Storage

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(
        default="https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg"
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        default="https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg",
        upload_to='images/', storage=S3Boto3Storage()
    )
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    is_private = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title

    def preview(self):
        return self.content[0:200]
    
class Contact(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    subject = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    date = models.DateField(default=timezone.now)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - From: {self.name} | {self.subject}"
