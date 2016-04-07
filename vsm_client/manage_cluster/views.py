from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    cluster_list = []
    for i in range(100):
        cluster = {
            "name":"cluster_name"+str(i),
            "status":"Active"
        }
        cluster_list.append(cluster);

    menu_list = set_menu("Cluster Management","Cluster")
    function_item = {"name":"Cluster List", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Cluster",function_item)
    return render(request, 
                "manage_cluster/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "cluster_list":cluster_list})


def add_view(request):
    menu_list = set_menu("Cluster Management","Cluster")
    function_item = {"name":"Add Cluster", "url":"/cluster/add/"}
    breadcrumb_list = set_breadcrumb("Cluster Management","Cluster",function_item)
    return render(request, 'manage_cluster/add.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})