from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from django.core.urlresolvers import reverse
from security.mixins import CompanySafeViewMixin
from security.utils import company_safe_form, company_safe_form_set


@login_required
def invoice_create(request):
    company = request.user.company

    invoice_form = forms.InvoiceCreateForm()
    item_sold_form_set = forms.ItemSoldFormSet()

    company_safe_form(invoice_form, company)
    company_safe_form_set(item_sold_form_set, company)

    if request.method == "POST":
        invoice_form = forms.InvoiceCreateForm(request.POST)
        item_sold_form_set = forms.ItemSoldFormSet(request.POST)

        if invoice_form.is_valid() and item_sold_form_set.is_valid():
            invoice = invoice_form.save(commit=False)
            invoice.company = company
            invoice.save()

            for item_sold_form in item_sold_form_set:
                item_sold = item_sold_form.save(commit=False)
                item = item_sold.item

                item_sold.company = company
                item_sold.invoice = invoice
                item_sold.name = item.name
                item_sold.tax = item.tax
                item_sold.price = item.price

                item_sold.save()

            return redirect('invoices:detail', pk=invoice.pk)



    context = {
        'invoice_form': invoice_form,
        'item_sold_form_set': item_sold_form_set,
    }
    return render(request, template_name='invoices/invoice_form.html', context=context)


class InvoiceDetailView(LoginRequiredMixin, CompanySafeViewMixin, DetailView):
    model = models.Invoice


class InvoiceListView(LoginRequiredMixin, CompanySafeViewMixin, ListView):
    model = models.Invoice
