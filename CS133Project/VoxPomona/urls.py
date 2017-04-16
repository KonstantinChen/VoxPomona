from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #User Profile
    url(r'^register', views.sign_up, name='register'),
    #url(r'^$', views.user_profile, name='user_profile'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #url(r'^profile', views.user_profile, name='user_profile'),
    #url(r'^logout', views.logout_view, name='logout_view'),
    # Login/Logout URLs

]