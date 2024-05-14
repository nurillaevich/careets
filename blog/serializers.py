from rest_framework import serializers
from .models import About, Team, Services, Author, Category, Tag, Blog, Comment


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer()
    categories = CategorySerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    blog = BlogSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
