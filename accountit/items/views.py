from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from rest_framework import generics
from .models import Item
from .forms import ItemCreateForm
from . import serializers


class ItemList(generics.ListCreateAPIView):
    serializer_class = serializers.ItemSerializer

    def get_queryset(self):
        company = self.request.user.company
        return Item.objects.all().filter(company=company)

    def perform_create(self, serializer):
        company = self.request.user.company
        serializer.save(company=company)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ItemSerializer

    def get_queryset(self):
        company = self.request.user.company
        return Item.objects.all().filter(company=company, pk=self.kwargs.get('pk'))


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemCreateForm

    def form_valid(self, form):
        item = form.save(commit=False)
        item.company = self.request.user.company
        item.save()
        self.object = item
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemCreateForm

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)


class ItemListView(LoginRequiredMixin, ListView):
    model = Item

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('items:list')

    def get_queryset(self):
        company = self.request.user.company
        query_set = super().get_queryset()
        return query_set.filter(company=company)
