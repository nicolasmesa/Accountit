from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Contact
from .forms import ContactCreateForm
from security.mixins import CompanySafeViewMixin


class ContactCreateView(LoginRequiredMixin, CompanySafeViewMixin, CreateView):
    model = Contact
    form_class = ContactCreateForm

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.company = self.request.user.company
        contact.save()
        self.object = contact
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, CompanySafeViewMixin, UpdateView):
    model = Contact
    form_class = ContactCreateForm


class ContactDetailView(LoginRequiredMixin, CompanySafeViewMixin, DetailView):
    model = Contact


class ContactListView(LoginRequiredMixin, CompanySafeViewMixin, ListView):
    model = Contact


class ContactDeleteView(LoginRequiredMixin, CompanySafeViewMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:list')
