var disk_capacity_chart, storage_group_chart, pg_chart, osd_chart;

function http_service(module,post_data,success_callback){
    $.ajax({
        type: "get",
        url: "/dashboard/overview/"+module+"/",
        data: post_data,
        dataType:"json",
        success: function(data){
            success_callback(data);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            switch(XMLHttpRequest.status == 401){
                case 401:
                        console.log("Unauthorized");
                    break;
                case 500:
                        console.log("internal server error");
                    break;
            }
        }
    });
}

function summary(data){
    if(data){
        $("#lblSummaryUptime").html(data.uptime);
        $("#lblSummaryVSMVersion").html(data.vsm_version);
        $("#lblSummaryCephVersion").html(data.ceph_version);
        $("#lblSummaryInstallTime").html(data.install_time);
    }
}

function disk_capacity(data){
    if(data){
        $("#lblDiskCapacityPercent").html(data.percent);
        $("#lblDiskCapacityTotal").html(data.total);
        $("#lblDiskCapacityUsed").html(data.used);
        $("#lblDiskCapacityUptime").html(data.uptime);

        if(disk_capacity_chart){
            //update the pie chart
            disk_capacity_chart
                .data(data.chart);

            disk_capacity_chart.render();
        }
        else{
            //draw the chart
            disk_capacity_chart = pieChart()
                .container("CapacityPie")
                .radius(50)
                .innerRadius(0)
                .data(data.chart);

            disk_capacity_chart.render();
        }
    }
}


function storage_group(data){
    if(data){
        $("#lblStorageGroupTotal").html(data.total);
        $("#lblStorageGroupHealth").html(data.health);
        $("#lblStorageGroupNearFull").html(data.nearfull);
        $("#lblStorageGroupFull").html(data.full);
        $("#lblStorageGroupUptime").html(data.uptime);

        if(storage_group_chart){
            //update the pie chart
            storage_group_chart
                .data(data.chart);

            storage_group_chart.render();
        }
        else{
            //draw the chart
            storage_group_chart = pieChart()
                .container("StorageGroupPie")
                .radius(50)
                .innerRadius(0)
                .data(data.chart);

            storage_group_chart.render();
        }
    }
}


function pg(data){
    if(data){
        $("#lblPGTotal").html(data.total);
        $("#lblPGActiveClean").html(data.active_clean);
        $("#lblPGNotActiveClean").html(data.not_active_clean);
        $("#lblPGUptime").html(data.uptime);

        if(pg_chart){
            //update the pie chart
            pg_chart
                .data(data.chart);

            pg_chart.render();
        }
        else{
            //draw the chart
            pg_chart = pieChart()
                .container("PGPie")
                .radius(50)
                .innerRadius(0)
                .data(data.chart);

            pg_chart.render();
        }
    }
}

function osd(data){
    if(data){
        $("#lblOSDInUp").html(data.in_up);
        $("#lblOSDInDown").html(data.in_down);
        $("#lblOSDOutUp").html(data.out_up);
        $("#lblOSDOutDown").html(data.out_down);
        $("#lblOSDEpoch").html(data.epoch);
        $("#lblOSDUptime").html(data.uptime);

        if(osd_chart){
            //update the pie chart
            osd_chart
                .data(data.chart);

            osd_chart.render();
        }
        else{
            //draw the chart
            osd_chart = pieChart()
                .container("OSDPie")
                .radius(50)
                .innerRadius(0)
                .data(data.chart);

            osd_chart.render();
        }
    }
}


function monitor(data){
    if(data){
        $("#lblMonitorProbing").html(data.probing);
        $("#lblMonitorElecting").html(data.electing);
        $("#lblMonitorSynchronizing").html(data.synchronizing);
        $("#lblMonitorLeader").html(data.leader);
        $("#lblMonitorPopen").html(data.popen);
        $("#lblMonitorEpoch").html(data.epoch);
        $("#lblMonitorUptime").html(data.uptime);
    }
}


function mds(data){
    if(data){
        $("#lblMDSIn").html(data.in);
        $("#lblMDSUp").html(data.up);
        $("#lblMDSStopped").html(data.stopped);
        $("#lblMDSFailed").html(data.failed);
        $("#lblMDSTotal").html(data.total);

        $("#lblMDSEpoch").html(data.epoch);
        $("#lblMDSMetaData").html(data.metadata);
        $("#lblMDSData").html(data.data);
        $("#lblMDSUptime").html(data.uptime);
    }
}


function iops(data){
    if(data){
        $("#lblIOPSWrite").html(data.write);
        $("#lblIOPSRead").html(data.read);
        $("#lblIOPSReadWrite").html(data.read_write);
        $("#lblIOPUptime").html(data.uptime);
    }
}


function lantency(data){
    if(data){
        $("#lblLantencyWrite").html(data.write);
        $("#lblLantencyRead").html(data.read);
        $("#lblLantencyReadWrite").html(data.read_write);
        $("#lblLantencyUptime").html(data.uptime);
    }
}

function bandwidth(data){
    if(data){
        $("#lblBandwidthIn").html(data.in);
        $("#lblBandwidthOut").html(data.out);
        $("#lblBandwidthUptime").html(data.uptime);
    }
}


function cpu(data){
    if(data){
        $("#lblCPUAverage").html(data.average);
        $("#lblCPUMaxIP").html(data.max_host);
        $("#lblCPUMax").html(data.max);
        $("#lblCPUMinIP").html(data.min_host);
        $("#lblCPUMin").html(data.min);
        $("#lblCPUUptime").html(data.uptime);
    }
}


