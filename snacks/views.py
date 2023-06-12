from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')



# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html' 