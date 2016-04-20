from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    menu_list = set_menu("Performance","Monitor")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Monitor",function_item)
    return render(request, 
                "performance_monitor/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
