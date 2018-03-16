$(document).ready(function() {
	$('form').submit(function(e) {
		e.preventDefault();

			$.ajax({
	    type: "POST",
	    url: "http://127.0.0.1:8000/sheduler/faculty/",
	    data: JSON.stringify({"name": $("#fname").val()}),
	    contentType: "application/json; charset=utf-8",
	    dataType: "json",
	    success: function(data,status) {
	        console.log(data);
	        $("#successMessage").text("You have successfully registered. Please login to continue");
	    },
	    error: function(data,status){
	        console.log(status);
	        var errorResponse = JSON.parse(data.responseText);
	        console.log(errorResponse.name[0]);
	        $("#errorfname").text(errorResponse.name[0]);
	    }
		});
	});
});


$(document).ready(function() {
	$('form').submit(function(e) {
		e.preventDefault();

			$.ajax({
	    type: "POST",
	    url: "http://127.0.0.1:8000/sheduler/semester/",
	    data: JSON.stringify({"semester_number": $("#semnumber").val(),"division":$("#division").val(),"class_location":$("#classnumber").val()}),
	    contentType: "application/json; charset=utf-8",
	    dataType: "json",
	    success: function(data,status) {
	        console.log(data);
	        $("#successMessage").text("You have successfully registered. Please login to continue");
	    },
	    error: function(data,status){
	        console.log(status);
	        var errorResponse = JSON.parse(data.responseText);
	        console.log(errorResponse);
	       
	    }
		});
	});
});