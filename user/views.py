from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Dashboard view
#@login_required         # A user must be logged in to see this view
def dashboard(request):
    return render(request, "user/dashboard.html")

# Music View
def music(request):
    return render(request, "user/music.html")

# Meditation View
def meditation(request):
    return render(request, "user/meditation.html")

# Mood View
def mood(request):
    return render(request, "user/mood.html")
