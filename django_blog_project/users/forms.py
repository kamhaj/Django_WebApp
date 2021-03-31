from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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