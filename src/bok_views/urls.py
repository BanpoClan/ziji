from django.conf.urls import url, include

from bok_views import index_views
from bok_views import user_views

urlpatterns = [
    url(r'^index/', index_views.index),
    url(r'^main_page/', index_views.main_page),
    url(r'^login/', user_views.login),
    url(r'^login_action/', user_views.login_action),
]
