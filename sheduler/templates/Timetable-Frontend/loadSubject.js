$(document).ready(function() {
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/sheduler/api/allSubject/",
			contentType: "application/json; charset=utf-8",
	    	dataType: "json",
	    success: function(data,status) {
	    	$("#list-of-subject-1").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-subject-1").append(`<option value="`+data[i].faculty+`" id="subject`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].subject_name+`</option>`);
	    	}
	    	$("#list-of-subject-2").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-subject-2").append(`<option id="subject`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].subject_name+`</option>`);
	    	}
	    	$("#list-of-subject-3").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-subject-3").append(`<option id="subject`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].subject_name+`</option>`);
	    	}
	    	$("#list-of-subject-4").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-subject-4").append(`<option id="subject`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].subject_name+`</option>`);
	    	}
	    	$("#list-of-subject-5").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-subject-5").append(`<option id="subject`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].subject_name+`</option>`);
	    	}
	    	$("#list-of-subject-6").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-subject-6").append(`<option id="subject`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].subject_name+`</option>`);
	    	}
	    },
	    error: function(data,status) {
	    	console.log(data);
	    	console.log(status);
	    }
		});
});

$(document).ready(function(){
	$.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/sheduler/api/allSubject/",
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		success:function(data,status){
			 /*$("#list-of-subject-1").change(function() {
        	
       		var a=data[1].subject_name;
       		console.log(a);
    });*/
			
			
		},
		error: function(data,status){
			console.log(data);
	    	console.log(status);
		},
	});

	$("#list-of-subject-1").change(function() {
        	$.ajax({
	    type: "GET",
		url: "http://127.0.0.1:8000/sheduler/api/allSubject/",
		contentType: "application/json; charset=utf-8",
		dataType: "json",
	    success: function(data,status) {
	    	var a=$("#list-of-subject-1 option:selected").val();
	    //    var b=$("#list-of-subject-1 option:selected").text();

	        $.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/sheduler/api/allFaculty/",
			contentType: "application/json; charset=utf-8",
	    	dataType: "json",
	    success: function(data,status) {
	    //	console.log(a,b);
	    	console.log(data);
	    	$.each(data,function (index, data) { 

	    		if((data.id)==a){

	    	//	$("#list-of-Faculty-1 option:selected").text(data.name);
	    		$("#list-of-Faculty-1 ").html(`<option id="faculty`+data.id+`" data-id="`+data.id+`">`+data.name+`</option>`);
	    		console.log(data.name);
	    	}

	    }); 
	    },
	   	
		});

		

	        
	    },
		});
    });
});


/*
$(document).ready(function() {
		$.ajax({
			type: "GET",
			url: "http://127.0.0.1:8000/sheduler/api/allFaculty/",
			contentType: "application/json; charset=utf-8",
	    	dataType: "json",
	    success: function(data,status) {
	    
	    	$("#list-of-Faculty-1").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-1").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    	$("#list-of-Faculty-2").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-2").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    	$("#list-of-Faculty-3").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-3").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    	$("#list-of-Faculty-4").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-4").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    	$("#list-of-Faculty-5").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-5").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    	$("#list-of-Faculty-6").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-6").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}

		
	    	$("#list-of-Faculty-7").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-7").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    	$("#list-of-Faculty-8").empty();
	    	for (var i = 0; i < data.length; i++) {
	    		$("#list-of-Faculty-8").append(`<option id="faculty`+data[i].id+`" data-id="`+data[i].id+`">`+data[i].name+`</option>`);
	    	}
	    },
	    error: function(data,status) {
	    	console.log(data);
	    	console.log(status);
	    }
		});
});

*/

