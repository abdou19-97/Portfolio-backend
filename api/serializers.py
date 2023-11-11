# import serializers from rest_framework
from rest_framework import serializers
# import Post and Comment models from api/models.py
from .models import Post, Comment

# create a serializer for Post and Comment models
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'content', 'post'