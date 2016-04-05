$(function(){
	//将pie分成，6块
	var numberOfDataPoint = 3,
	    data = [];

	data = d3.range(numberOfDataPoint).map(function (i) {
	    return {id: i, value: randomData()};
	});

	var chart1 = pieChart()
	        .container("CapacityPie")
	        .radius(50)
	        .innerRadius(0)
	        //.colors(["red","blue","yellow","green"])
	        .data(data);

	chart1.render();

	var chart2 = pieChart()
	        .container("StorageGroupPie")
	        .radius(50)
	        .innerRadius(0)
	        //.colors(["red","blue","yellow","green"])
	        .data(data);

	chart2.render();


	var chart3 = pieChart()
	        .container("PGPie")
	        .radius(50)
	        .innerRadius(0)
	        //.colors(["red","blue","yellow","green"])
	        .data(data);

	chart3.render();


	var chart3 = pieChart()
	        .container("OSDPie")
	        .radius(50)
	        .innerRadius(0)
	        //.colors(["red","blue","yellow","green"])
	        .data(data);

	chart3.render();


})