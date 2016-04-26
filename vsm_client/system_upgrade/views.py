from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    menu_list = set_menu("Cluster Management","Ceph Upgrade")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Ceph Upgrade",function_item)
    return render(request, 
                "system_upgrade/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
