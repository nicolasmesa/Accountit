from django.conf.urls import url
from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.ContactListView.as_view(), name='list'),
    url(r'^create/$', views.ContactCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)$', views.ContactUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)$', views.ContactDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)$', views.ContactDeleteView.as_view(), name='delete'),
]

urlpatterns = [
    url(r'^$', views.ContactList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ContactDetail.as_view(), name='contact-detail'),
]
