"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('page1/',views.page1, name='page1'),
    path('page2/',views.page2, name='page2'),
    path('page3/',views.page3, name='page3'),
    path('page4/',views.page4, name='page4'),
    path('page5/',views.page5, name='page5'),
    path('login/',views.login, name='login')
    
]
