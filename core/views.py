from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            if not email or User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists or Email is left empty")
                return redirect("signup")

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                # log user in and redirect to settings page.

                # create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("signup")  # will make it login page later
        else:
            messages.info(request, "Passwords do not match")
            return redirect("signup")
    else:
        return render(request, "signup.html")
