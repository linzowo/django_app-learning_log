# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

def check_topic_owner(topic,request):
    """check topic = owner"""
    if topic.owner != request.user:
        raise Http404

def index(request):  #问题：这个函数中的参数从什么地方来
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')


def topics(request):
    """当用户处于登陆状态时显示自己的私有主题和所以公开主题
    当用户未登录时显示所有公开主题"""
    if request.user.is_authenticated():
        topics = Topic.objects.filter(Q(owner=request.user) | Q(public=True)).order_by('date_added')
    else:
        topics = Topic.objects.filter(public=True).order_by('date_added')

    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目"""
    topic = get_object_or_404(Topic,id=topic_id)
    #confirm that the subject of the request belongs to the current user
    check_topic_owner(topic,request)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    """添加新的主题"""
    if request.method != 'POST':
        #没有提交数据，创建一个新的表格
        form = TopicForm()
    else:
        #post提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    """在用户添加的特定主题下添加内容"""
    topic = get_object_or_404(Topic,id=topic_id)

    if request.method != 'POST':
        #如果用户没有提交数据
        form = EntryForm()
    else:
        #post提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            #check_topic_owner(topic,request)
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑现有的条目"""
    entry = get_object_or_404(Entry,id=entry_id)
    topic = entry.topic
    check_topic_owner(topic,request)

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form =EntryForm(instance=entry)
    else:
        #post提交数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)



