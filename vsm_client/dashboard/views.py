# _*_ coding: utf-8 _*_
from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb
from django.utils.translation import ugettext_lazy  as _

def index(request):
    menu_list = set_menu("Dashboard","")
    function_item = {"name":"", "url":""}
    name = _("XuShouan")
    breadcrumb_list = set_breadcrumb("Dashboard","",function_item)
    return render(request, 'dashboard/index.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list,"name":name})