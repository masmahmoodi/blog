from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post

# Create your views here.

@api_view(["GET"])
def ping(request):
    return Response({"status": "ok"})

@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)