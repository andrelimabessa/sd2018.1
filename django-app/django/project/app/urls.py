from django.conf.urls import include, url
from . import views
from . import admin

urlpatterns = [
    url(r'jogar/$', views.post_list),
    url('', views.iniciar),
]