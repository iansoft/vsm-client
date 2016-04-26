from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    ec_profile_list = []
    for i in range(20):
        ec_profile = {
            "name":"profile."+str(i),
            "plugin_name":"plugin_name_"+str(i),
            "plugin_path":"plugin_path_"+str(i),
            "pg_number":"10",
            "Key_Value":"{\"k\":2,\"m\":1,\"technique\":\"reed_sol_van\"}"
        }
        ec_profile_list.append(ec_profile);

    menu_list = set_menu("Cluster Management","EC Profile")
    function_item = {"name":"EC Profile", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","EC Profile",function_item)
    return render(request, 
                "manage_ec_profile/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "ec_profile_list":ec_profile_list})


def add_ec_profile_view(request):
    menu_list = set_menu("Cluster Management","EC Profile")
    function_item = {"name":"EC Profile", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","EC Profile",function_item)
    return render(request, 
                "manage_ec_profile/add_ec_profile.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
