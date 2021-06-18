from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import registrationForm

# class edit(SuccessMessageMixin,LoginView):
#     template_name = 'edit/edit.html'
#     success_message = 'Successfully registered'




class RegisterView(SuccessMessageMixin,CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = registrationForm
    success_url = reverse_lazy('login')
    success_message = 'Successfully registered'


class SignInView(SuccessMessageMixin,LoginView):
    template_name = 'account/login.html'
    # success_url = reverse_lazy('home')
    success_message = 'Successfully sign-up'

# class ProfileView(DetailView):
#     model =  User
#     template_name = 'account/profile.html'

def profile(request):

    return render(request, 'account/profile.html')







