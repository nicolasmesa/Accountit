from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . import models


class UserDetailsRegistrationForm(forms.ModelForm):
    class Meta():
        model = models.UserDetails
        fields = ('name',)


class CompanyRegistrationForm(forms.ModelForm):
    class Meta():
        model = models.Company
        fields = ('name',)

    # Setup a label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Company name'



class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    # Setup a label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'