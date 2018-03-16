$(document).ready(function() {
	$('form').submit(function(e) {
		e.preventDefault();

			$.ajax({
	    type: "POST",
	    url: "http://127.0.0.1:8000/sheduler/users/",
	    data: JSON.stringify({"email": $("#newUsername").val(),"password": $("#newUserPassword").val()}),
	    contentType: "application/json; charset=utf-8",
	    dataType: "json",
	    success: function(data,status) {
	        console.log(data);
	        $("#successMessage").text("You have successfully registered. Please login to continue");
	    },
	    error: function(data,status){
	        console.log(status);
	        var errorResponse = JSON.parse(data.responseText);
	        console.log(errorResponse.email[0]);
	        $("#emailError").text(errorResponse.email[0]);
	    }
		});
	});
});