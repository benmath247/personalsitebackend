from django.contrib import admin
from .models import *

# Register your models here.

models = [Blog, Category, Contact, Tag]

for model in models:
    admin.site.register(model)
