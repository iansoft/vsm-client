from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    menu_list = set_menu("Integrate","Openstack")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("Integrate","Openstack",function_item)
    return render(request, 
                "integrate_openstack/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
