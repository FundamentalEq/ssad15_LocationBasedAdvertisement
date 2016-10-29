"""ssad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = [
    url(r'^ssad15/', include('ssad15.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^userauth/', include('userauth.urls')),
    # url(r'^user/password/reset/$',
    #     'django.contrib.auth.views.password_reset',
    #     {'post_reset_redirect' : '/user/password/reset/done/'},
    #     name="password_reset"),
    # (r'^user/password/reset/done/$',
    #     'django.contrib.auth.views.password_reset_done'),
    # (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     'django.contrib.auth.views.password_reset_confirm',
    #     {'post_reset_redirect' : '/user/password/done/'}),
    # (r'^user/password/done/$',
    #     'django.contrib.auth.views.password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
