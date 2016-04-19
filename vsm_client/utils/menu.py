# _*_ coding: utf-8 _*_

menu_list = [
	{"name":"Dashboard", "url":"/home/", "icon":"fa-dashboard", "openable":False,"active":"","children":[]},
	#{"name":"i18n", "url":"/i18n/", "icon":"fa-dashboard", "openable":False,"active":"","children":[]},
	{"name":"Cluster Management", "url":"/cluster/", "icon":"fa-cloud", "openable":True,"active":"","children":[
		{"name":"Cluster", "url":"/cluster/","icon":"fa-star", "openable":False,"active":"","children":[]},
		{"name":"Server", "url":"/server/","icon":"fa-desktop", "openable":False,"active":"","children":[]},
		{"name":"Device", "url":"/home/","icon":"fa-plus", "openable":False,"active":"","children":[]},
		{"name":"Pool", "url":"/home/","icon":"fa-database", "openable":False,"active":"","children":[]},
		{"name":"RBD", "url":"/home/","icon":"fa-database", "openable":False,"active":"","children":[]},
		{"name":"Storage Group", "url":"/home/","icon":"fa-users", "openable":False,"active":"","children":[]},
		{"name":"Zone", "url":"/home/","icon":"fa-sitemap", "openable":False,"active":"","children":[]}
	]},
	{"name":"Performance", "url":"/home/", "icon":"fa-bar-chart-o", "openable":True,"active":"","children":[
		{"name":"OSD", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
		{"name":"Monitor", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
		{"name":"MDS", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
		{"name":"PG", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
		{"name":"Pool", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
		{"name":"RBD", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
		{"name":"Storage Group", "url":"/home/","icon":"fa-arrows", "openable":False,"active":"","children":[]},
	]},
	{"name":"Openstack Integration", "url":"", "icon":"fa-external-link", "openable":True,"active":"","children":[
		{"name":"RBD Pool", "url":"/account/","icon":"fa-database", "openable":False,"active":"","children":[]},
		{"name":"Openstack Access", "url":"/home/","icon":"fa-retweet", "openable":False,"active":"","children":[]}
	]},
	{"name":"System Management", "url":"/home/", "icon":"fa-cogs", "openable":True,"active":"","children":[
		{"name":"Settings", "url":"/home/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
		{"name":"User", "url":"/home/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
		{"name":"Role", "url":"/home/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
		{"name":"Ceph Upgrade", "url":"/home/","icon":"fa-file-text-o", "openable":False,"active":"","children":[]},
	]}
]

def set_menu(parent_menu_name, sub_menu_name):
	for menu in menu_list:
		menu["active"] = ""
		if menu["name"] == parent_menu_name:
			menu["active"] = "active"
			for sub_menu in menu["children"]:
				sub_menu["active"] = ""
				if sub_menu["name"] == sub_menu_name:
					sub_menu["active"] = "active"
	return menu_list


def set_breadcrumb(parent_menu_name, sub_menu_name, function_item):
	breadcrumb_list = []
	for menu in menu_list:
		if menu["name"] == parent_menu_name:
			breadcrumb_list.append(menu)
			for sub_menu in menu["children"]:
				if sub_menu["name"] == sub_menu_name:
					breadcrumb_list.append(sub_menu)
	breadcrumb_list.append(function_item)
	return breadcrumb_list