from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
# Create your views here.

def sign_up(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("post_list")
    else:
        form = SignUpForm()
    context = {
        "form": form
    }
    return render(request, "account/signup.html",  context)