"""BLOG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

from blog import views
from blog.views import (
    home_page,
    article_page,
    category_page,
    create_article,
    add_comment,
    registration,
    user_login,
    article_search,
    about_page,
    single_post_page,
    pages_page,
    contact_page,
    author_page,
    profile,
    profile_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home_page"),
    path("blog/<slug:slug>/", article_page, name="article_page"),
    path("blog/category/<slug:category>/", category_page, name="category_page"),
    path("blog/author/<slug:author_name>/", author_page, name="author_page"),
    path("create/", create_article, name="create_article"),
    path("article/<int:article_id>/add_comment/", add_comment, name="add_comment"),
    path("article-like/<int:article_id>/", views.article_like, name="article_like"),
    path("registration/", registration, name="registration"),
    path('profile-view/', profile_view, name='profile-view'),
    path('profile-edit/', profile, name='profile'),
    path("login/", user_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("search/", article_search, name="article_search"),
    path("about/", about_page, name="about_page"),
    path("single_post/", single_post_page, name="single_post_page"),
    path("pages/", pages_page, name="pages_page"),
    path("contact/", contact_page, name="contact_page"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("newsletter", views.newsletter, name="newsletter"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
