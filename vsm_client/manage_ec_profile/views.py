from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    ec_profile_list = []
    for i in range(100):
        ec_profile = {
            "name":"osd."+str(i),
            "server":"server_"+str(i),
            "storage_class":"class",
            "zone":"zone1",
            "status":"Active",
        }
        ec_profile_list.append(ec_profile);

    menu_list = set_menu("Cluster Management","EC Profile")
    function_item = {"name":"EC Profile", "url":""}
    breadcrumb_list = set_breadcrumb("Cluster Management","EC Profile",function_item)
    return render(request, 
                "manage_ec_profile/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list, "ec_profile_list":ec_profile_list})
