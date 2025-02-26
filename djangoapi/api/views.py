from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost, SecondaryPost
from .serializers import BlogPostSerializer, SecondaryPostSerializer
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

  def delete(self, request, *args, **kwargs):
    BlogPost.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = "pk"

# class BlogPostList(APIView):
#   def get(self, request, format=None):

class SecondaryPostListCreate(generics.ListCreateAPIView):
  queryset = SecondaryPost.objects.all()
  serializer_class = SecondaryPostSerializer
  lookup_field = "pk"
