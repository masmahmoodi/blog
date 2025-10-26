# from django.contrib import admin
from django.urls import path
from .views import post_list,post_detail,make_post , edit_comment, post_edit, delete_post,my_posts, delete_comment, like_post


urlpatterns = [
    path("", post_list, name="post_list"),
    path("post_detail/<slug:slug>/", post_detail, name="post_detail"),
    path("post/new", make_post, name="make_post"),
    path("post/edit/<slug:slug>", post_edit , name="post_edit"),
    path("post/delete/<slug:slug>", delete_post, name="delete_post" ),
    path("my_posts/", my_posts, name="my_posts"),
    path("comment/edit/<int:comment_id>/", edit_comment, name="edit_comment"),
    path("comment/delete/<int:comment_id>/", delete_comment, name="delete_comment"),
    path("posts/<slug:slug>/like/", like_post, name="like_post")
    ]

