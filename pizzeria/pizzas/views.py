# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Pizza
def index(request):
    """披萨店主页"""
    return render(request,'pizzas/index.html')

def menu(request):
    """披萨店菜单页"""
    pizzas = Pizza.objects.order_by('-date_added')
    context = {'pizzas':pizzas}
    return render(request,'pizzas/menu.html',context)

def topping(request,pizza_id):
    """披萨的配料"""
    pizza = Pizza.objectes.get(id=pizza_id)
    topping = pizza.entry_set.order_by('date_added')
    context = {'pizza':pizza,'topping':topping}
    return render(request,'pizzas/topping.html',context)