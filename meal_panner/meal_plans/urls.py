#_*_ coding:utf-8 _*_
"""定义meal_plans的URL模型"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #主页
    url(r'^$',views.index,name='index'),
    ]