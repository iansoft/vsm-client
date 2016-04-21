from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    server_list = []
    for i in range(20):
        server = {
            "id":i,
            "name":"server_name"+str(i),
            "management_ip":"192.168.1."+str(i),
            "public_ip":"192.168.1."+str(i),
            "cluster_ip":"192.168.1."+str(i),
            "monitor":True,
            "zone":"zone_"+str(i),
            "osd_amount":i*10,
            "status":"Active",
        }
        server_list.append(server);

    menu_list = set_menu("Cluster Management","Server")
    function_item = {"name":"Server List", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Server",function_item)
    return render(request, 
                "manage_server/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "server_list":server_list})


def detail_view(request,id):
    menu_list = set_menu("Cluster Management","Server")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Server",function_item)

    server = {
        "basic":{
            "id":id,
            "name":"Server 001",
            "zone":"zone",
            "status":"Active",
            "monitor":True,
            "osd_amount":10,
            "MDS":True,
        },
        "system":{
            "OS":"Ubuntu 14.04 LTS",
        },
        "hardware":{
            "cpu":"Intel(R) Core(TM) i5-4250U CPU @ 1.3GHz 1.90GHz",
            "RAM":"128.0 GB(84.5 GB usable)",
            "system_type":"64-bit"
        },
        "network":{
            "management_ip":"192.168.1.10",
            "public_ip":"192.168.2.10",
            "cluster_ip":"192.168.3.10",
        },
        "OSD":{

        },
        "monitor":{

        },
        "MDS":{

        }
    }
    return render(request, 'manage_server/detail.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list,"server":server})

def add_view(request):
    menu_list = set_menu("Cluster Management","Server")
    function_item = {"name":"Add Server", "url":"/server/add/"}
    breadcrumb_list = set_breadcrumb("Cluster Management","Server",function_item)
    return render(request, 'manage_server/add.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
