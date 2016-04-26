from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    device_list = []
    for i in range(10):
        device = {
            "name":"osd."+str(i),
            "server":"server_"+str(i),
            "storage_class":"class",
            "zone":"zone1",
            "weight":2,
            "capacity":"12.0 GB/24.0 GB(50%)",
            "status":"Active",
        }
        device_list.append(device);

    menu_list = set_menu("Server Management","Device")
    function_item = {"name":"Device List", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Device",function_item)
    return render(request, 
                "manage_device/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "device_list":device_list})


def add_view(request):
    menu_list = set_menu("Server Management","Device")
    function_item = {"name":"Add Device", "url":"/device/add/"}
    breadcrumb_list = set_breadcrumb("Cluster Management","Device",function_item)
    return render(request, 'manage_device/add.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})


def import_view(request):
    menu_list = set_menu("Server Management","Device")
    function_item = {"name":"Import Device", "url":"/device/import/"}
    breadcrumb_list = set_breadcrumb("Cluster Management","Device",function_item)
    return render(request, 'manage_device/import.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})