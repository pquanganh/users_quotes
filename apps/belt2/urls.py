from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^register$', views.register),
url(r'login$', views.login),
url(r'^quotes$', views.quotes),
url(r'^logout$', views.logout),
url(r'^add_quote$', views.add_quote),
url(r'^(?P<id>\d+)/user$', views.user),
url(r'^(?P<id>\d+)/add_fav$', views.add_fav),
url(r'^(?P<id>\d+)/rm_fav$', views.rm_fav),
]