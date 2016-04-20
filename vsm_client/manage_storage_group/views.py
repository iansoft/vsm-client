from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    menu_list = set_menu("Cluster Management","Storage Group")
    function_item = {"name":"Storage Group", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Storage Group",function_item)
    return render(request, 
                "manage_storage_group/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
