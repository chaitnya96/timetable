$(document).ready(function() {
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/sheduler/api/allFaculty/",
			contentType: "application/json; charset=utf-8",
	    	dataType: "json",
	    success: function(data,status) {
	    	for (var i = 0; i < data.length; i++) {
	    		$("#faculty").append(`<option value="`+data[i].id+`" >`+data[i].name+`</span><br>`);
	    		console.log($("span").val());
	    	}
	    	
	    },
	    error: function(data,status) {
	    	console.log(data);
	    	console.log(status);
	    }
		});
});