from .models import About, Team, Services, Author, Category, Tag, Blog, Comment
from .serializers import AboutSerializer, TeamSerializer, ServiceSerializer, AuthorSerializer, CategorySerializer, \
    TagSerializer, BlogSerializer, CommentSerializer

from rest_framework import generics


class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ServiceList(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
