from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from rest_framework import permissions
from rest_framework import generics
from .models import Contact
from .forms import ContactCreateForm
from . import serializers
from security.mixins import CompanySafeViewMixin


class ContactList(generics.ListCreateAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        company = self.request.user.company
        return Contact.objects.all().filter(company=company)

    def perform_create(self, serializer):
        company = self.request.user.company
        serializer.save(company=company)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        company = self.request.user.company
        return Contact.objects.all().filter(pk=self.kwargs.get('pk'), company=company)


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
