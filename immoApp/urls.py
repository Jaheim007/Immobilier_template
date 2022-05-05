from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('blog', views.blogGrid , name='blog'),
    path('blogSingle', views.blogSingle , name='blogSingle'),
    path('agentSingle', views.agentSingle , name='agentSingle'),
    path('agentGrid', views.agentGrid , name='agentGrid'),
    path('contact', views.contact , name='contact'),
    path('property', views.propertyGrid , name='property'),
    path('propertySingle', views.propertySingle , name='propertySingle'),
]
