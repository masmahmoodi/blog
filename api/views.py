from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer
from blog.models import Post

# ✅ added: DRF permissions (login required to write, read allowed for all)
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # <-- added
from rest_framework.decorators import permission_classes          # <-- added


@api_view(["GET"])
def ping(request):
    return Response({"status": "ok"})


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])  # <-- added: read-only for anon, auth required to POST
def post_list(request):

    if request.method == "POST":
        # ✅ added: pass context (future-proof for Hyperlinked serializers)
        serializer = PostSerializer(data=request.data, context={'request': request})  # <-- changed

        if serializer.is_valid():
            # ✅ added: set author from logged-in user if your model/serializer supports it
            try:  # avoids TypeError if 'author' isn't a writable field
                serializer.save(author=request.user)  # <-- added
            except TypeError:
                serializer.save()                     # <-- added (fallback)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ changed: deterministic ordering; using '-id' (safe) instead of assuming 'created_at'
    posts = Post.objects.all().order_by('-id')  # <-- changed

    paginator = PageNumberPagination()
    posts = paginator.paginate_queryset(posts, request)

    # ✅ added: pass context on list as well
    serializer = PostSerializer(posts, many=True, context={'request': request})  # <-- changed
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])  # <-- added: only authenticated can modify/delete
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "PUT":
        # ✅ added: pass context
        serializer = PostSerializer(post, data=request.data, context={'request': request})  # <-- changed
        if serializer.is_valid():
            serializer.save()  # author unchanged here; adjust if you want to lock author
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        # ✅ added: pass context; partial=True already correct
        serializer = PostSerializer(post, data=request.data, partial=True, context={'request': request})  # <-- changed
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        post.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

 
    serializer = PostSerializer(post, context={'request': request})  # <-- changed
    return Response(serializer.data)
