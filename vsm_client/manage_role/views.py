from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    role_list = []
    for i in range(20):
        role = {
            "name":"user name "+str(i),
            "group":"develop",
            "enable":True,
        }
        role_list.append(role)


    menu_list = set_menu("System Management","Role")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("System Management","Role",function_item)
    return render(request, 
                "manage_role/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list,"role_list":role_list})
