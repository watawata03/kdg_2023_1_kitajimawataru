from django.shortcuts import render
from django.views.generic import ListView
from .models import Rebels

class ListRebelsView(ListView):
    template_name = 'rebels/index.html'
    model = Rebels

class ListCompanyView(ListView):
    template_name = 'rebels/company.html'
    model = Rebels

class ListServiceView(ListView):
    template_name = 'rebels/service.html'
    model = Rebels

class ListFaqView(ListView):
    template_name = 'rebels/faq.html'
    model = Rebels

class ListContactView(ListView):
    template_name = 'rebels/contact.html'
    model = Rebels

class ListService80View(ListView):
    template_name = 'rebels/service2.html'
    model = Rebels

class ListService1View(ListView):
    template_name = 'rebels/service1.html'
    model = Rebels

class ListService2View(ListView):
    template_name = 'rebels/service2.html'
    model = Rebels

class ListService3View(ListView):
    template_name = 'rebels/service3.html'
    model = Rebels

class ListService4View(ListView):
    template_name = 'rebels/service4.html'
    model = Rebels

class ListService5View(ListView):
    template_name = 'rebels/service5.html'
    model = Rebels

class ListService6View(ListView):
    template_name = 'rebels/service6.html'
    model = Rebels
    
class ListLoginView(ListView):
    template_name = '/accounts/login'
    model = Rebels


    