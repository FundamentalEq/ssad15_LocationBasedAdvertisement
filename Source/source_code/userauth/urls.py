from django.conf.urls import url, include
from django.contrib.auth.views import password_reset, password_reset_complete, password_reset_confirm, password_reset_done
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^$', views.home, name='home'),
    url(r'^device/$', views.device_login, name='device_login'),
    # url( r'^user-autocomplete/$',views.autocompleteUser.as_view(),name='user-autocomplete'),
    url(r'^password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'},name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^password_reset_complete/$', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},name='password_reset_complete'),
    url(r'^register_edit/(?P<pk>\d+)/edit/$', views.user_edit, name='register_edit'),
    url(r'^history/$', views.user_history, name='user_history'),
    url(r'^total_cost/$', views.total_cost, name='total_cost'),
    url(r'^not_confirm_cost/$', views.not_confirm_cost, name='not_confirm_cost'),
]
