# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:07:14 2020

@author: Humberto
"""

from blogging.models import Post, Category
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'created_date', 'modified_date', 'published_date', 'categories']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']