from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^start_advertisement/$', views.start_advertisement, name='start_advertisement'),
    url(r'^display_advertisement/$', views.display_advertisement, name='display_advertisement'),
    url(r'^render_advertisement/$', views.render_advertisement, name='render_advertisement'),
    url(r'^invalid_location/', views.invalid_location ),
    url(r'^unauthorised_access/', views.unauthorised_access ),
    url(r'^invalid_empty_database/', views.invalid_empty_database ),
    url(r'^internal_server_error/',views.internal_server_error),
    url(r'^edit_zone/(?P<longitude>\d+\.?\d*)/(?P<latitude>\d+\.?\d*)/',views.edit_zone, name='edit_zone'),
    url(r'^select_zone/$', views.select_zone, name='select_zone'),
    url(r'^index/$', views.index, name='index')
]
