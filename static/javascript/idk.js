function send(){
	var login = {'username':$("#username")[0].value, //get username and password values from webpage via its id and create login object
				 'password':$("#password")[0].value
				};

	$.ajax({
		type: "POST",
		url: "/login", //name of python method
		data: login,
		success: function(data){
			var res = data['res'];
			$("#status")[0].innerHTML="[ Status: "+res+" ]";
			window.location.href = "{{ url_for('template',filename = file:///home/anusha/blooddonation/LookUpBloodDB/templates/select.html) }}"

		},
		error: function(data){
			$("#status")[0].innerHTML="[ Status: Login failure ]";
		}
	});
}