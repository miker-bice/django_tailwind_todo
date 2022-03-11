from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'loginApp/login.html', )


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.email):
                form.save()
                # messages.success(request, f'Hi {username}, your account has been successfully added')
                return redirect('loginApp:login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'loginApp/register.html', context)
