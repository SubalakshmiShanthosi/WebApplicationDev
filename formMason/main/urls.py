# app/urls.py
from django.conf.urls import url
from main.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view() , name='home' ),
]
