# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:58:59 2020

@author: Humberto
"""

from django.urls import path
from blogging.views import stub_view
from blogging.views import list_view
from blogging.views import detail_view
from blogging.views import add_model

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('add_post/', add_model, name="blog_add_post"),
]