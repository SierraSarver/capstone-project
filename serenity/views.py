from django.shortcuts import render, redirect
from user.custom_forms import RegisterUserForm
from user.custom_forms import SignUpForm

# If user is logged in, return the dashboard view. Else, return the landing page.
# Will just go to landing page when starting django server since not logged in.
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, "serenity/landing-page.html")

# Need a function here to render signup view form login button click
def signup_view(request):
        #detect get or post
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            (request.POST)
            #check if form is valid
            if form.is_valid():
                user = form.save()
                #log the user in after
                #redirect to /home
                return redirect('user_login')
            else:
                return render(request, 'serenity/signup-form.html', {'form1':form})
        #if get, return a blank form
        else:
            form = RegisterUserForm()
        return render(request, 'serenity/signup-form.html/', {'form1':form})
