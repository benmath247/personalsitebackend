from blog.views import blog_list
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    # path("", views.home, name="home"),
    path("blog/", views.blog_list, name="blog"),
    path("blog/<int:id>/", views.blog_detail, name="blog_detail"),
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    path("blog/private/", views.private_blog_list, name="private"),
    path("blog/category/<str:name>/", views.blogs_in_category, name="blog_category_list"),
    path('blog/tag/<str:tag_name>/', views.tag_posts, name='tag_posts'),
    path("category/<str:name>/", views.category_detail, name="category_detail"),
    path("category/", views.category_list, name="category_list"),
    path("blog/author/<str:username>/", views.blogs_from_author, name="blog_author_list"),
    path("author/<str:username>/", views.author_detail, name="author_detail"),
    path("contact/", views.contact, name="contact"),
    path("", views.home, name='home')
]
