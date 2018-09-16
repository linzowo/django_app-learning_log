#-*- coding:utf-8 -*-
"""����pizzas��URLģ�͵��ļ�"""

from django.conf.urls import url
from . import views

urlpatterns = [
    #��������ҳ
    url(r'^$',views.index,name='index'),

    #������˵�
    url(r'^menu/$',views.menu,name='menu'),

    #�������ϱ�
    url(r'^menu/(?P<pizza_id>\d+)/$',views.topping,name='topping'),
    ]