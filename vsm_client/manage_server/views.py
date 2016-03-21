from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    server_list = []
    for i in range(100):
        server = {
            "name":"server_name"+str(i),
            "public_ip":"192.168.1."+str(i),
            "status":"Active"
        }
        server_list.append(server);

    menu_list = set_menu("Cluster Management","Server")
    function_item = {"name":"Server List", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Server",function_item)
    return render(request, 
                "manage_server/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "server_list":server_list})


def add_view(request):
    menu_list = set_menu("Cluster Management","Server")
    function_item = {"name":"Add Server", "url":"/server/add/"}
    breadcrumb_list = set_breadcrumb("Cluster Management","Server",function_item)
    return render(request, 'manage_server/add.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
