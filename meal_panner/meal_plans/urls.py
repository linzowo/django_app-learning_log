#_*_ coding:utf-8 _*_
"""����meal_plans��URLģ��"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #��ҳ
    url(r'^$',views.index,name='index'),
    ]