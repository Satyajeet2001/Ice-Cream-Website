from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('buy', views.buy, name='buy'),
    path('contact', views.contact, name='contact')
]
