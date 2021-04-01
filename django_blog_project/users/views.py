from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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


## show profile info and update if you want
@login_required()       ## to force being logged in to see this profile.html template
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # request.POST for user generated info to be passed to our form
        p_form = ProfileUpdateForm(request.POST,                      # request.FILES to catch an image uploaded by used
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  ## redirect is a GET method, we will not have "POST/GET redirect pattern" problem
    else:
        u_form = UserUpdateForm(instance=request.user)  # instance will populate a form with current User info (filled in from the start)
        p_form = ProfileUpdateForm(instance=request.user.profile)  # instance will populate a form with current Profile info (filled in from the start)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)