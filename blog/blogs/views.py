# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import BlogPost
from .forms import PostNoteForm
def index(request):
    """博客主页"""
    notes = BlogPost.objects.order_by('date_added')
    context = {'notes':notes}
    return render(request,'blogs/index.html',context)

def show_note(request,note_id):
    """显示具体的博客内容"""
    note = BlogPost.objects.get(id=note_id)
    context = {'note':note}
    return render(request,'blogs/show_note.html',context)

@login_required
def new_note(request):
    """添加新帖子"""
    if request.method != 'POST':
        #还没提交数据的时候
        form = PostNoteForm()
    else:
        form = PostNoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = request.user
            new_note.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form':form}
    return render(request,'blogs/new_note.html',context)

@login_required
def edit_note(request,note_id):
    """编辑已有帖子"""
    note = BlogPost.objects.get(id=note_id)

    if note.owner == request.user:
        if request.method != 'POST':
            #初次请求使用已有内容填充表单
            form = PostNoteForm(instance=note)
        else:
            #post提交的数据对数据进行处理
            form = PostNoteForm(instance=note,data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('blogs:index'))

        context = {'note':note,'form':form}
        return render(request,'blogs/edit_note.html',context)
    else:
        raise Http404
