from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from fform import views


urlpatterns = [
    url(r'^$', views.home, name='post'),
   # url(r'^postt/$', views.postt),
    url(r'^postnew/$', views.postnew),
    url(r'^postnew1/$', views.postnew1),
    url(r'^postnew2/$', views.postnew2),
    url(r'^postnew3/$', views.postnew3),
    url(r'^post/$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
