from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    device_list = []
    for i in range(100):
        device = {
            "name":"osd."+str(i),
            "server":"server_"+str(i),
            "storage_class":"class",
            "zone":"zone1",
            "status":"Active",
        }
        device_list.append(device);

    menu_list = set_menu("Cluster Management","Device")
    function_item = {"name":"Device List", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Device",function_item)
    return render(request, 
                "manage_device/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "device_list":device_list})
