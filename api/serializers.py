from blog.models import Post

from rest_framework import serializers



from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'likes', 'body', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'author', 'likes', 'created_at', 'updated_at']
