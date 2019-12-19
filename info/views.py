from django.shortcuts import render
from django.views.generic import ListView
from .models import Account
# Create your views here.

class HomeListView(ListView):
    model = Account
    template_name = 'index.html'

class ProfileListView(ListView):
    model = Account
    template_name = 'profile.html'

class ContactListView(ListView):
    model = Account
    template_name = 'contact.html'


