# Functions to handle the different views for a new or returning Serenity user.
#   - Takes HTTP requests and returns some response
#       - Generally calles a template and/or Model

# https://docs.djangoproject.com/en/2.0/topics/forms/
#   Reference for learning Django's custom forms

from django.shortcuts import render, redirect
from user.custom_forms import RegisterUserForm

# Function to handle the different views between users who are
# authenticated and those who are not.
def landing_page(request):
    # if user is logged in, return the dashboard view
    if request.user.is_authenticated:
        return redirect('dashboard')
    # else, return the landing page since user is not authenticated
    else:
        return render(request, "serenity/landing-page.html")
        # will render landing page when starting server since new user

# Function to instantiate the custom registration form into the signup view.
def signup_view(request):
    # if it is a post request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request
        form = RegisterUserForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # save it
            user = form.save()
            # redirect the user to login
            return redirect('user_login')
    # else if it is a get request, return a blank form
        # expect this on first time visit
    else:
        form = RegisterUserForm()
    return render(request, 'serenity/signup-form.html/', {'form1':form})
