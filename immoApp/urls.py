from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about' ),
    path('blogGrid', views.blogGrid , name='blogGrid'),
    path('blogSingle', views.blogSingle , name='blogSingle'),
    path('agentSingle', views.agentSingle , name='agentSingle'),
    path('agentGrid', views.agentGrid , name='agentGrid'),
    path('Contact', views.contact , name='contact'),
    path('propertyGrid', views.propertyGrid , name='propertyGrid'),
    path('propertySingle', views.propertySingle , name='propertySingle'),
]
