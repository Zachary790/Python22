from django.urls import path
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session)
]
