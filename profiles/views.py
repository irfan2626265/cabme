from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import CreateView,TemplateView,UpdateView
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import User
from django.contrib.auth.views import LoginView


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/accounts/login/'


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class DashboardView(TemplateView):
    template_name = 'profiles/dashboard.html'


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.request.user.profile
        context['userprofile'] = user_profile
        return context


class UserProfileUpdateView(UpdateView):
    template_name = 'profiles/update_profile.html'
    model = User
    fields = ['username','password','email'] 
    success_url = '/accounts/profile/'





