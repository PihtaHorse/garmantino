# -*- coding: utf-8 -*-
"""GarmantinoBy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.garmantino import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^askquestion/$', views.AskQuestionView.as_view(), name='ask_question'),
    url(r'^catalogue/$', views.CatalogueView.as_view(), name='catalogue'),
    url(r'^catalogue/category/(?P<category_id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.ItemView.as_view(), name='item'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
