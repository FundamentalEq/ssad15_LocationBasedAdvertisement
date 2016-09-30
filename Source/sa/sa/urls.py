from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test
from django.conf.urls.static import static
import django.contrib.auth.views
admin.autodiscover()
login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userauth/', include('userauth.urls')),
    #url(r'^accounts/login/$', django.contrib.auth.views.login,name='login'),
    #url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
