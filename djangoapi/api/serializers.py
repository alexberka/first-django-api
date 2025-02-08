from rest_framework import serializers
from .models import BlogPost, SecondaryPost

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    fields = ['id', 'title', 'content', 'published_date']

class SecondaryPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = SecondaryPost
    fields = ['id', 'title', 'content', 'published_date']
