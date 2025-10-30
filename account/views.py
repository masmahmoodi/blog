from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Profile 
# Create your views here.

def sign_up(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user, defaults={"name":user.username})
            login(request,user)
            return redirect("post_list")
    else:
        form = SignUpForm()
    context = {
        "form": form
    }
    return render(request, "account/signup.html",  context)

@login_required
def profile(request):
    profile, _ =  Profile.objects.get_or_create(user=request.user, defaults={"name":request.user.username})
    context = {
        "profile": profile
    }
    return render(request, "account/profile.html", context)
