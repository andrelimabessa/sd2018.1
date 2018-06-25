from django.conf.urls import include, url
from . import views
from . import admin

urlpatterns = [
    url(r'teste/$', views.post_list),
]