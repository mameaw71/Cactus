# Create your views here.
#from django.http import HttpResponse

#def homePageView(request):
    #return HttpResponse('Hello, World')

from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home.html'

def page1(request):    
    return render(request, 'page1.html')
def page2(request):    
    return render(request, 'page2.html')
def page3(request):    
    return render(request, 'page3.html')
def page4(request):    
    return render(request, 'page4.html')
def page5(request):    
    return render(request, 'page5.html')
def login(request):    
    return render(request, 'login.html')

