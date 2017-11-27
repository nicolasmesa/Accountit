from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.core.urlresolvers import reverse


def user_register(request):
    user_form = forms.UserRegistrationForm()
    company_form = forms.CompanyRegistrationForm()


    if request.method == "POST":
        user_form = forms.UserRegistrationForm(request.POST)
        company_form = forms.CompanyRegistrationForm(request.POST)

        if user_form.is_valid() and company_form.is_valid():
            user = user_form.save(commit=False)

            # User who creates the account is admin
            user.is_admin = True
            company = company_form.save()
            user.company = company
            user.save()

            return redirect('home')


    context = {
        'company_form': company_form,
        'user_form': user_form,
    }
    return render(request, template_name='accounts/signup.html', context=context)


class UserCreate(LoginRequiredMixin, CreateView):
    form_class = forms.UserCreateForm
    model = get_user_model()

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        company = self.request.user.company
        self.object = form.save(commit=False)
        self.object.company = company
        self.object.save()
        return super().form_valid(form)

