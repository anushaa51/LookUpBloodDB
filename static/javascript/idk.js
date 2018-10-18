function login(){
	var login = {'username':$("#username")[0].value, //get username and password values from webpage via its id and create login object
				 'password':$("#password")[0].value
				};

	$.ajax({
		type: "POST",
		url: "/login", //name of python method
		data: login,
		success: function(response){
		 				$('html').html(response);
		 			}
		});
}