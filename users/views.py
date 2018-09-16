# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """register new user"""
    if request.method != 'POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #process filled out forms
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #allow users to log in automatically and redirect to the home page
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)