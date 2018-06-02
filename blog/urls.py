from django.contrib import admin
from django.conf.urls import url
from . import views

#admin.autodiscover()
urlpatterns = [
    url(r'^$', views.homePage),
    url(r'^blog/(?P<username>\w+)/$',views.blog),
    url(r'^blog/(?P<username>\w+)/(?P<year>\d+)/$',views.year_post),
    url(r'^blog/(?P<username>\w+)/(?P<year>\d+)/(?P<month>\w+)/$',views.month_post),
    url(r'^user/(?P<username>\w+)/$',views.user),
    url(r'^post/(?P<id>\d+)/$',views.post),
    ]
