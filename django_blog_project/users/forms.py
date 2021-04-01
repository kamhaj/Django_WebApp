from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile ## cos we need a Profile.picture


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default required=True

    '''
    this nested class gives us a nasted namespaces for configurations
    and keeps these configurations in one place
    model that will be affected is User model (so model.save() will save it to User model)
    '''
    class Meta():
        model = User
        ## fileds we want to have in our form (in this order)
        fields = ['username', 'email', 'password1', 'password2']


## to allow User to update Profile (just email and username, password in a different way - via email)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # default required=True

    class Meta():
        model = User
        ## fileds we want to have in our form (in this order)
        fields = ['username', 'email']


## to allow User to update Profile (image) - different Form required since User does not have an image field, Profile does
## but if we puth both form in a template, its gonna look like one form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']