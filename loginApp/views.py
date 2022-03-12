from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('todoApp:home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todoApp:home')
        else:
            form = AuthenticationForm()
            messages.error(request, f"Invalid Username or Password")
            return render(request, 'loginApp/login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'loginApp/login.html', {'form': form})

    # if request.user.is_authenticated:
    #     return redirect('todoApp:home')
    #
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         return redirect('todoApp:home')
    #     else:
    #         form = AuthenticationForm()
    #         return render(request, 'loginApp/login.html', {'form': form})
    #
    # else:
    #     form = AuthenticationForm()
    #     return render(request, 'loginApp/login.html', {'form': form})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('todoApp:home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been successfully added')
            return redirect('loginApp:login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'loginApp/register.html', context)
