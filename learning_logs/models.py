# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """管理内容的模型"""
    topic = models.ForeignKey(Topic)  #通过外键链接到主题
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        """以字符串返回用户的输入内容"""
        return self.text[:50] + '...'