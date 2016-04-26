from django.shortcuts import render
from utils.menu import set_menu,set_breadcrumb

def index(request):
    account_list = []
    for i in range(20):
        account = {
            "name":"user name "+str(i),
            "group":"develop",
            "role":"admin",
        }
        account_list.append(account)

    menu_list = set_menu("System Management","Account")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("System Management","Account",function_item)
    return render(request, 
                "manage_account/index.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list,"account_list":account_list})


def create_view(request):
    menu_list = set_menu("System Management","Account")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("System Management","Account",function_item)
    return render(request, 
                "manage_account/add.html",
                {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})
