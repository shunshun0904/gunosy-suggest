from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello_guess_category, name = 'hello_guess_category'),
]