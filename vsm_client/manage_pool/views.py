from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    pool_list = []
    for i in range(100):
        pool = {
            "name":"pool."+str(i),
            "storage_group":"group.1",
            "pg_amount":3,
            "size":"50",
            "quota":"5G",
            "status":"Active",
        }
        pool_list.append(pool);

    menu_list = set_menu("Cluster Management","Pool")
    function_item = {"name":"Pool List", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Pool",function_item)
    return render(request, 
                "manage_pool/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "pool_list":pool_list})


def create_replicated_pool_view(request):
    menu_list = set_menu("Cluster Management","Pool")
    function_item = {"name":"Create Replicated Pool", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Pool",function_item)
    return render(request, 
                "manage_pool/add_replicated_pool.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})


def create_ec_pool_view(request):
    menu_list = set_menu("Cluster Management","Pool")
    function_item = {"name":"Create Replicated Pool", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Pool",function_item)
    return render(request, 
                "manage_pool/add_ec_pool.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})

def add_cache_tier_view(request):
    menu_list = set_menu("Cluster Management","Pool")
    function_item = {"name":"Add Cache Tier", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","Pool",function_item)
    return render(request, 
                "manage_pool/add_cache_tier.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})