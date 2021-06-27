''' we are importing from Django path function and ALL OUR VIEWS'''
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

### first URL pattern

URLPattern = [
    path('', views.post_list, name = 'post_list')
]