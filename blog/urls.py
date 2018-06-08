from django.contrib import admin
from django.conf.urls import url
from . import views

#admin.autodiscover()
urlpatterns = [
    url(r'^$', views.homePage),
    url(r'^blog/(?P<username>\w+)/$',views.blog),
    url(r'^blog/(?P<username>\w+)/(?P<year>\d+)/$',views.year_post),
    url(r'^blog/(?P<username>\w+)/(?P<year>\d+)/(?P<month>\d+)/$',views.month_post),
    url(r'^user/(?P<username>\w+)/$',views.user, name="profile"),
    url(r'^post/(?P<id>\d+)/$',views.post),
    url(r'^register/$',views.userRegister.as_view()),
    url(r'^post/new/$', views.addPost),
    url(r'^post/(?P<id>\d+)/edit/$',views.editPost),
    url(r'^post/(?P<id>\d+)/delete/$',views.deletePost),
    url(r'^post/(?P<id>\d+)/comment/new/$',views.comment),
    url(r'^info/$',views.info),
    ]
