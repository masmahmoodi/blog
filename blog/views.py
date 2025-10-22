from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Comment
# Create your views here.
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    comments = post.comments.all()

    if request.method == "POST":
        pass
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect("post_detail", slug=post.slug)
        
    
    comment = CommentForm()
    context = {
        "post": post,
        "comment":comment,
        "comments": comments,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "blog/make_post.html"  , {"form":form})



def post_edit(request,slug):
    post= Post.objects.get(slug=slug)
    if request.method == "POST":
         form =PostForm(data=request.POST,instance=post)
         if form.is_valid():
             form.save()
             return redirect("post_list")
    else:
        form = PostForm(instance=post)
    return render(request,"blog/edit_post.html", {"form":form})



def delete_post(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method=="POST":
        post.delete()
        return redirect('post_list')
    return render(request,"blog/delete_post.html", {"post":post})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author = request.user)
    return render(request, "blog/my_posts.html", {"posts":posts})



def edit_comment(request,comment_id):
    comment  = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail",slug=comment.post.slug )
    form = CommentForm(instance=comment)
    return render(request, "blog/edit_comment.html", {"form":form})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_slug = comment.post.slug
    if request.method == "POST":
        comment.delete()
        return redirect("post_detail", slug=post_slug)
    return render(request, "blog/delete_comment.html", {"comment": comment})