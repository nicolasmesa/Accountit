"""accountit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import HomeView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^items/', include('items.urls', namespace='items')),
    url(r'^invoices/', include('invoices.urls', namespace='invoices')),

]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/v1/contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^api/v1/items/', include('items.urls', namespace='items')),
    url(r'^api/v1/invoices/', include('invoices.urls', namespace='invoices')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/v1/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/v1/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
