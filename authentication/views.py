from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib import messages


class OrderForm(ModelForm):
    class Meta:
        
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create your views here.
def homepage(request) :
    return render(request, 'authentication/home.html')

def signuppage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')

            return redirect('login')
        

    context = {'form': form}
    return render(request, 'authentication/reg.html', context)

    

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'authentication/login.html')
    context = {}        
    return render(request, 'authentication/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')

            return redirect('login')
        

    context = {'form': form}
    return render(request, 'authentication/registration.html', context )