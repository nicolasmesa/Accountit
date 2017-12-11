from django.conf.urls import url
from . import views

app_name = 'items'


urlpatterns = [
    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^create/$', views.ItemCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)$', views.ItemUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)$', views.ItemDeleteView.as_view(), name='delete'),
]


urlpatterns = [
    url(r'^$', views.ItemList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ItemDetail.as_view(), name='item-detail'),
]