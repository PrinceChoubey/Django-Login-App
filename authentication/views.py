from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate ,login ,logout

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')

def signup(request):

    if request.method =='POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, 'Username already exist')
        if User.objects.filter(email=email):
            messages.error(request, 'Email already exists.')

        if password==password2:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = FirstName
            myuser.last_name = LastName

            myuser.save()
            messages.success(request, "Your account has been sign up successfully.")
            return redirect('signin')
    return render(request,'authentication/signup.html')


def signin(request):
    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(username=username1,password=password1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname':fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    return render(request,'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully.')
    return redirect('home')