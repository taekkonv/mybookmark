from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BookmarkListV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetailV.as_view(), name='detail'),
]
