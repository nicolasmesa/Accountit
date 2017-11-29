from django import forms
from django.forms import formset_factory
from .models import Invoice, ItemSold

class InvoiceCreateForm(forms.ModelForm):
    class Meta():
        model = Invoice
        exclude = ('company', 'items')


class ItemSoldForm(forms.ModelForm):
    class Meta():
        model = ItemSold
        fields = ('item', 'quantity')


ItemSoldFormSet = formset_factory(ItemSoldForm)
