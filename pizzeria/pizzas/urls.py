#-*- coding:utf-8 -*-
"""管理pizzas的URL模型的文件"""

from django.conf.urls import url
from . import views

urlpatterns = [
    #披萨店主页
    url(r'^$',views.index,name='index'),

    #披萨店菜单
    url(r'^menu/$',views.menu,name='menu'),

    #披萨配料表
    url(r'^menu/(?P<pizza_id>\d+)/$',views.topping,name='topping'),
    ]