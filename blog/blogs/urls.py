#-*- coding:utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns =[
    #主页
    url(r'^$',views.index,name='index'),

    #查看博客内容
    url(r'^(?P<note_id>\d+)/$',views.show_note,name='show_note'),

    #添加新的博客内容
    url(r'^new_note/$',views.new_note,name='new_note'),

    #编辑已有内容
    url(r'^edit_note/(?P<note_id>\d+)/$',views.edit_note,name='edit_note'),
    ]