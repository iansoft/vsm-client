# _*_ coding: utf-8 _*_
from __future__ import division 
import time,datetime
import json
import random
from django.shortcuts import render
from django.http import HttpResponse
from utils.menu import set_menu,set_breadcrumb
from utils.time import get_time_delta
from django.utils.translation import ugettext_lazy  as _

def index(request):
    menu_list = set_menu("Dashboard","")
    function_item = {"name":"", "url":""}
    breadcrumb_list = set_breadcrumb("Dashboard","",function_item)
    return render(request, 'dashboard/index.html', {"menu_list":menu_list, "breadcrumb_list":breadcrumb_list})

def overview(request, module):
    #the response data
    data = {}

    if module == "summary":
        data = summary()
    elif module == "disk_capacity":
        data = disk_capacity()
    elif module == "storage_group":
        data = storage_group()
    elif module == "pg":
        data = pg()
    elif module == "server":
        pass
    elif module == "osd":
        data = osd()
    elif module == "monitor":
        data = monitor()
    elif module == "mds":
        data = mds()
    elif module == "iops":
        data = iops()
    elif module == "lantency":
        data = lantency()
    elif module == "bandwidth":
        data = bandwidth()
    elif module == "cpu":
        data = cpu()
    return HttpResponse(json.dumps(data))

def summary():
    return {
        "vsm_version":"v3.0.0",
        "ceph_version":"v10.0.4 ",
        "install_time":"2015.09.01",
        "uptime":now()
    }

def disk_capacity():
    total = 100;
    used = random.randint(60,total)
    percent = used / total;
    return {
        "total":"4G 500MB",
        "used":"2G 500MB",
        "percent":str(percent) + "%",
        "uptime":now(),
        "chart":[
            {"name":"normal", "value":(total - used)},
            {"name":"used", "value":used},
        ]
    }

def storage_group():
    percent_data = percent();
    return {
        "total":percent_data["total"],
        "health":percent_data["health"],
        "nearfull":percent_data["nearfull"],
        "full":percent_data["full"],
        "uptime":now(),
        "chart":[
            {"name":"health", "value":percent_data["health"]},
            {"name":"nearfull", "value":percent_data["nearfull"]},
            {"name":"full", "value":percent_data["full"]},
        ]
    }

def pg():
    total = 100;
    active_clean = random.randint(60,total)
    not_active_clean = total - active_clean
    return {
        "total":total,
        "active_clean":active_clean,
        "not_active_clean":not_active_clean,
        "uptime":now(),
        "chart":[
            {"name":"active_clean", "value":active_clean},
            {"name":"not_active_clean", "value":not_active_clean},
        ]
    }

def osd():
    total = 100
    in_up = random.randint(0,total)
    in_down = random.randint(0,(total-in_up))
    out_up = random.randint(0,(total-in_up-in_down))
    out_down = random.randint(0,(total-in_up-in_down-out_up))
    percent_data = percent();
    return {
        "in_up":in_up,
        "in_down":in_down,
        "out_up":out_up,
        "out_down":out_down,
        "epoch":"2.2",
        "uptime":now(),
        "chart":[
            {"name":"health", "value":percent_data["health"]},
            {"name":"nearfull", "value":percent_data["nearfull"]},
            {"name":"full", "value":percent_data["full"]},
        ]
    }

def monitor():
    return {
        "probing":random.randint(0,100),
        "electing":random.randint(0,100),
        "synchronizing":random.randint(0,100),
        "leader":random.randint(0,100),
        "popen":random.randint(0,100),
        "epoch":"2.2",
        "uptime":now(),
    }

def mds():
    return {
        "in":random.randint(0,100),
        "up":random.randint(0,100),
        "stopped":random.randint(0,100),
        "failed":random.randint(0,100),
        "total":random.randint(0,100),
        "metadata":"2.2",
        "data":"232.2",
        "epoch":"422.2",
        "uptime":now(),
    }

def iops():
    return {
        "write":random.randint(0,100),
        "read":random.randint(0,100),
        "read_write":random.randint(0,100),
        "uptime":now(),
    }

def lantency():
    return {
        "write":random.randint(0,100),
        "read":random.randint(0,100),
        "read_write":random.randint(0,100),
        "uptime":now()
    }

def bandwidth():
    return {
        "in":random.randint(0,100),
        "out":random.randint(0,100),
        "uptime":now()
    }

def cpu():
    return {
        "average":random.randint(0,100),
        "max":random.randint(0,100),
        "max_host":"192.168.1.%s" % (str(random.randint(1,255))),
        "min":random.randint(0,100),
        "min_host":"192.168.1.%s" % (str(random.randint(1,255))),
        "uptime":now()
    }

def percent():
    total = 100;
    health = random.randint(60,total)
    nearfull = random.randint(0,(total-health))
    full = total-health-nearfull
    return {
        "total":total,
        "health":health,
        "nearfull":nearfull,
        "full":full
    }

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
