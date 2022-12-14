from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """New user registration"""
    if request.user.is_authenticated:
        return redirect('recipes:index')
    else:
        if request.method == 'POST':
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                login(request, new_user)
                return redirect('recipes:index')
        else:
            form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)