from django.shortcuts import render, redirect
from . import models
from . import forms


def user_create(request):
    user_form = forms.UserCreateForm()
    company_form = forms.CompanyRegistrationForm()


    if request.method == "POST":
        user_form = forms.UserCreateForm(request.POST)
        company_form = forms.CompanyRegistrationForm(request.POST)

        if user_form.is_valid() and company_form.is_valid():
            user = user_form.save()
            company = company_form.save()

            return redirect('home')


    context = {
        'company_form': company_form,
        'user_form': user_form,
    }
    return render(request, template_name='accounts/signup.html', context=context)
