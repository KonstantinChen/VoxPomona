from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #User Profile
    #url(r'^create-user', views.create_user, name='create_user'),
    #url(r'^$', views.user_profile, name='user_profile'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #url(r'^profile', views.user_profile, name='user_profile'),
    #url(r'^logout', views.logout_view, name='logout_view'),

]