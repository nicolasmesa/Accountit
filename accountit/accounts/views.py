from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from . import forms
from . import serializers
from . import permissions as custom_permissions


User = get_user_model()


class UsersList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsAdminOrReadOnly, )
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        company = self.request.user.company
        return User.objects.all().filter(company=company)

    def perform_create(self, serializer):
        company = self.request.user.company
        serializer.save(company=company)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.or_based([custom_permissions.IsOwnerOrReadOnly, custom_permissions.IsAdmin]),
        custom_permissions.CannotDeleteSelf,
    )
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        company = self.request.user.company
        return User.objects.all().filter(pk=self.kwargs.get('pk'), company=company)


class CompanyDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (
        custom_permissions.IsAdminOrReadOnly,
    )
    serializer_class = serializers.CompanySerializer

    def get_object(self):
        return self.request.user.company



class AccountCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        company_serializer = serializers.CompanySerializer(data=request.data)
        user_serializer = serializers.UserSerializer(data=request.data)

        company_serializer.is_valid(raise_exception=True)
        user_serializer.is_valid(raise_exception=True)

        company = company_serializer.save()
        user_serializer.save(company=company)

        return Response(company_serializer.data, status=status.HTTP_201_CREATED)


# Non API
def user_register(request):
    user_form = forms.UserRegistrationForm()
    company_form = forms.CompanyRegistrationForm()


    if request.method == "POST":
        user_form = forms.UserRegistrationForm(request.POST)
        company_form = forms.CompanyRegistrationForm(request.POST)

        if user_form.is_valid() and company_form.is_valid():
            user = user_form.save(commit=False)

            # User who creates the account is admin
            user.is_admin = True
            company = company_form.save()
            user.company = company
            user.save()

            return redirect('home')


    context = {
        'company_form': company_form,
        'user_form': user_form,
    }
    return render(request, template_name='accounts/signup.html', context=context)


class UserCreate(LoginRequiredMixin, CreateView):
    form_class = forms.UserCreateForm
    model = get_user_model()

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        company = self.request.user.company
        self.object = form.save(commit=False)
        self.object.company = company
        self.object.save()
        return super().form_valid(form)

