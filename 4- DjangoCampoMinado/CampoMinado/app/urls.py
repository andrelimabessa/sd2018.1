from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'inicio/$', views.iniciar),
	url(r'jogada', views.efetuar_jogada),
	url(r'principal', views.principal),
    path('', views.iniciar, name='inicio'),
]