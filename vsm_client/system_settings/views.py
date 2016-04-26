from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    settings_list = [
        {"name":"STORAGE_GROUP_NEAR_FULL_THRESHOLD","value":"68","enable":-1},
        {"name":"STORAGE_GROUP_FULL_THRESHOLD","value":"85","enable":-1},
        {"name":"DISK_NEAR_FULL_THRESHOLD","value":"75","enable":-1},
        {"name":"DISK_FULL_THRESHOLD","value":"90","enable":-1},
        {"name":"CPU_DIAMOND_COLLECT_INTERVAL","value":"15","enable": 0},
        {"name":"CEPH_DIAMOND_COLLECT_INTERVAL","value":"15","enable":1},
        {"name":"KEEP_PERFORMANCE_DATA_DAYS","value":"7","enable":-1},
    ]
    menu_list = set_menu("System Management","Settings")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("System Management","Settings",function_item)
    return render(request, 
                "system_settings/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list,"settings_list":settings_list})
