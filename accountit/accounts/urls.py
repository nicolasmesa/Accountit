from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.user_register, name='signup'),
    url(r'^create/$', views.UserCreate.as_view(), name='create'),
]


urlpatterns = [
    url(r'^$', views.AccountCreate.as_view(), name='account-create'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name="user-detail"),
    url(r'^users/$', views.UsersList.as_view(), name='list'),
    url(r'^company/$', views.CompanyDetail.as_view(), name='company-detail'),
]