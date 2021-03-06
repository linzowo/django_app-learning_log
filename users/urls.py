#_*_ coding:utf_8 _*_
"""为应用程序users定义url模式"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #登录界面
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    #注销界面
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册界面
    url(r'^register/$',views.register,name='register'),
]