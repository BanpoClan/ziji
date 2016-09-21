from django.conf.urls import url, include

from bok_views import index_views

urlpatterns = [
    url(r'^index/', index_views.index),
    url(r'^main_page/', index_views.main_page),
]
