from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^start_advertisement/$', views.start_advertisement, name='start_advertisement'),
    url(r'^display_advertisement/$', views.display_advertisement, name='display_advertisement')
]
