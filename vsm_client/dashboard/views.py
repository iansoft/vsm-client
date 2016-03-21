# _*_ coding: utf-8 _*_
from django.shortcuts import render
from utils.menu import set_menu

def index(request):
    menu_list = set_menu("Dashboard","")
    return render(request, 'dashboard/index.html', {'name': '徐守安',"menu_list":menu_list})