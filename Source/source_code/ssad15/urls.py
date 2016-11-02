from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^start_advertisement/$', views.start_advertisement, name='start_advertisement'),
    url(r'^display_advertisement/$', views.display_advertisement, name='display_advertisement'),
    url(r'^render_advertisement/$', views.render_advertisement, name='render_advertisement'),
    url(r'^edit_zone/(?P<zone_no>\d+)/',views.edit_zone, name='edit_zone'),
    url(r'^select_zone/$', views.select_zone, name='select_zone'),
    url(r'^index/$', views.index, name='index')
]
