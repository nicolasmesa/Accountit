from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact
from .forms import ContactCreateForm


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactCreateForm

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.company = self.request.user.company
        contact.save()
        self.object = contact
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactCreateForm

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)


class ContactListView(ListView):
    model = Contact

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = 'contacts:list'

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)
