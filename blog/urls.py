from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
	#path('', views.post_list, name='post_list'),
	
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
]