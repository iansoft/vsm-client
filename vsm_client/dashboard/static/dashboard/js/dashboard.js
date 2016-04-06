$(function(){

	setInterval(function(){
		http_service("summary",null, summary);
		http_service("disk_capacity",null, disk_capacity);
		http_service("storage_group",null, storage_group);
		http_service("pg",null, pg);
		http_service("osd",null, osd);
		http_service("monitor",null, monitor);
		http_service("mds",null, mds);
		http_service("iops",null, iops);
		http_service("lantency",null, lantency);
		http_service("bandwidth",null, bandwidth);
		http_service("cpu",null, cpu);
	},1000);
	
})

