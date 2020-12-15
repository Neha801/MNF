from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.template.defaultfilters import slugify
from .decorators import unauthenticated_user

from django.contrib.auth.models import User


# Create your views here.


def signup_view(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)

            messages.success(request, 'Account was created for ')
            return redirect('users:login')

    return render(request, 'login/signup.html', {'form': form})


@unauthenticated_user
def login_view(request):
    print("get")
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        # username = User.objects.get(email=email)
        # calendar = get_object_or_404(Calendar, slug=calendar_slug)

        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('palak:script_info')
            
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    
    return render(request, 'login/signin.html', context)

def logoutUser(request):
    logout(request)
    return redirect('users:login')


def forgot_password(request):
    return render(request, 'login/forgot.html')
