from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.shortcuts import render
from .models import *
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import json
from django.conf import settings

import boto3
from botocore.client import Config

###
# blog views
###


def blog_list(request):
    blogs = Blog.objects.filter(is_private=False).order_by("-pub_date")
    blog_list = []
    for blog in blogs:
        s3 = boto3.client('s3',
                            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                            region_name=settings.AWS_S3_REGION_NAME,
                            config=Config(signature_version='s3v4'))
        url = s3.generate_presigned_url('get_object',
                                        Params={'Bucket': 'benmathdotio',
                                                'Key': 'images/' + str(blog.image)},
                                        ExpiresIn=3600)
        # import pdb;pdb.set_trace()
        blog_dict = {
            "id": blog.id,
            "image": str(blog.image.url),
            "title": blog.title,
            "content": blog.content,
            "pub_date": blog.pub_date,
            "author": blog.author.username,
            "categories": [category.name for category in blog.categories.all()],
        }
        blog_list.append(blog_dict)
    return JsonResponse({"blogs": blog_list})

def private_blog_list(request):
    blogs = Blog.objects.filter(is_private=True)
    blog_list = []
    for blog in blogs:
        blog_dict = {
            "id": blog.id,
            "image": str(blog.image),
            "title": blog.title,
            "content": blog.content,
            "pub_date": blog.pub_date,
            "author": blog.author.username,
            "categories": [category.name for category in blog.categories.all()],
        }
        blog_list.append(blog_dict)
    return JsonResponse({"blogs": blog_list})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    blog_dict = {
        "title": blog.title,
        "image": str(blog.image),
        "content": blog.content,
        "pub_date": blog.pub_date,
        "author": blog.author.username,
        "categories": [category.name for category in blog.categories.all()],
    }
    return JsonResponse(blog_dict)
    # return render(request, "blog/blog_detail.html", {"blog": blog})


###
# category views
###


def blogs_in_category(request, name):
    category = Category.objects.get(name=name)
    blogs = Blog.objects.filter(categories=category, is_private=False)
    # data = serializers.serialize("json", blogs)
    blog_dict = {
        "category": {"name": category.name, "image": str(category.image)},
        "blogs": list(blogs.values()),
    }
    return JsonResponse(blog_dict)
    # return render(request, "blog/blog_list.html", {"blogs": blogs})


def category_detail(request, name):
    category = Category.objects.get(name=name)
    # data = serializers.serialize("json", category)
    return HttpResponse(category, content_type="application/json")


def category_list(request):
    categories = Category.objects.all()
    data = serializers.serialize("json", categories)
    return HttpResponse(data, content_type="application/json")


###
# author views
###


def blogs_from_author(request, username):
    user = User.objects.get(username=username)
    blogs = Blog.objects.filter(author=user, is_private=False)
    # data = serializers.serialize("json", blogs)
    blog_dict = {
        "author": {
            "username": user.username,
        },
        "blogs": list(blogs.values()),
    }
    return JsonResponse(blog_dict)


def author_detail(request, username):
    user = User.objects.filter(username=username)
    # data = serializers.serialize("json", user)
    return HttpResponse(user, content_type="application/json")


def home(request):
    return render(request, "blog/home.html")


@api_view(['GET', 'POST'])
def contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
            'Contact us form entry',
            'Benmath.io got a new contact form entry! go to the admin panel to take a look.',
            'ben@benmath.io',
            ['ben@benmath.io'],
            fail_silently=False,)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def tag_posts(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    blogs = Blog.objects.filter(tags=tag).filter(is_private=False)
    # data = serializers.serialize('json', posts)


    blog_list = []
    for blog in blogs:
        blog_dict = {
            "id": blog.id,
            "image": str(blog.image),
            "title": blog.title,
            "content": blog.content,
            "pub_date": blog.pub_date,
            "author": blog.author.username,
            "categories": [category.name for category in blog.categories.all()],
            "tags": [tag.name for tag in blog.tags.all()]
        }
        blog_list.append(blog_dict)
    data = {
        "tag": tag_name,
        "blogs": blog_dict
    }
    return JsonResponse(data, safe=False)