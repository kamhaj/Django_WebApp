from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # check if user-provided data is valid
        if form.is_valid():
            form.save()     # auto-handle stuff like password hash
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} - your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


## show profile info
@login_required()       ## to force being logged in to see this profile.html template
def profile(request):
    return render(request, 'users/profile.html')