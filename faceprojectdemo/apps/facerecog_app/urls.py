from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^createuser$', views.newuser),
    url(r'^login$', views.login),
    url(r'^demo$', views.demo),
]