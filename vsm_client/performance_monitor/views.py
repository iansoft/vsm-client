from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    menu_list = set_menu("Performance","Monitor")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Monitor",function_item)
    return render(request, 
                "performance_monitor/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list,
                 "storage_group_list":storage_group_status()})


def storage_group_status():
    storage_group_list = []
    for i in range(20):
        storage_group = {
            "name":"storage group "+str(i),
            "pool":i*10,
            "capacity_used":"20.32 GB/40.64 GB (50%)",
            "max_node_used":"30.32 GB/60.64 GB (50%)",
            "status":"health",
            "update_at":"2016-04-26 12:12:12"
        }
        storage_group_list.append(storage_group)
    return storage_group_list