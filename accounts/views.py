from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords not match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    # Login after register
                    # login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')                    
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You Have Registed Successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', {})

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)         
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
            
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid Login')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})    

def auth_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
        #return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})
