from django.shortcuts import render, redirect  
from django.contrib.auth import login  
from django.contrib import messages  
from .forms import CustomUserCreationForm  

def signup(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            messages.success(request, "Account created successfully!")  
            return redirect('profile')  
        else:  
            messages.error(request, "Registration failed. Fix errors below.")  
    else:  
        form = CustomUserCreationForm()  
    return render(request, 'users/signup.html', {'form': form})  

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    context = {
        'email': user.email,
        'last_login': user.last_login,
    }
    return render(request, 'users/profile.html', context)
