from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from django.contrib.auth.decorators import login_required

# Create your views here.

def home (request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password= password)
        if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('home')
        else:
             messages.success(request, "There was an error logging in. Please try again!")
             return redirect('login')
    else:  
        return render(request, 'website/home.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
     return render(request, 'register.html')