__author__ = 'Mateus'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^users$', views.users),
    url(r'^customers$', views.customers),
    url(r'^products$', views.products),
    url(r'^features$', views.features),
    url(r'^booking', views.booking),
]