from django.conf.urls import url
from . import views

app_name = 'riddles'

urlpattern = [
    url(r'^$', views.index, name='index')
]
