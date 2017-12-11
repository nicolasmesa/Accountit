from django.conf.urls import url
from . import views


app_name = 'invoices'


urlpatterns = [
    url(r'^$', views.InvoiceListView.as_view(), name='list'),
    url(r'^create/', views.invoice_create, name='create'),
    url(r'^detail/(?P<pk>\d+)$', views.InvoiceDetailView.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', views.InvoiceList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.InvoiceDetail.as_view(), name='invoice-detail'),
]