# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pizza(models.Model):
    """管理披萨的模型"""
    name = models.CharField(max_length=200)  #管理披萨名字的属性
    date_added = models.DateTimeField(auto_now_add=True)  #自动在属性后添加时间
    
    def __unicode__(self):
        """返回字符串格式的披萨名字"""
        return  self.name

class Topping(models.Model):
    """管理配料的模型"""
    pizza = models.ForeignKey(Pizza)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topping'

    def __unicode__(self):
        """返回字符串格式的配料内容"""
        if len(self.name)>50:
            return self.name[:50] + '...'
        else:
            return self.name