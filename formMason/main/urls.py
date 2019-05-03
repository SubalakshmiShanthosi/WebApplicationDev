from django.conf.urls import url
from main.views import CustomFormView
from main.views import HomePageView
from main.views import FormResponsesListView

app_name = 'main'

urlpatterns = [
    url(r'^$', HomePageView.as_view() , name='home' ),
    url(r'^form/(?P<form_pk>\d+)/$', CustomFormView.as_view(),name='custom-form'),
    url(r'^form/(?P<form_pk>\d+)/responses/$', FormResponsesListView.as_view(), name='form-responses'),
]
