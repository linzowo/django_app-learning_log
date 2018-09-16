# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def logout_view(request):
    """log off user"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

def register(request):
    """register a new user"""
    if request.method != 'POST':
        #show empty registy
        form = UserCreationForm()
    else:
        #process filled out form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #allow user login automatically and redircte to home page
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)