from django import forms
from . import models


class ContactCreateForm(forms.ModelForm):
    class Meta():
        model = models.Contact
        exclude = ('company',)