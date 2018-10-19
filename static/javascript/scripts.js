var loginglobal;

function login(){
	var login = {'username':$("#username")[0].value, //get username and password values from webpage via its id and create login object
				 'password':$("#password")[0].value
				};
	window.loginglobal = login;

	$.ajax({
		async:true,
		type: "POST",
		url: "/login", //name of python method
		data: login,
		success: function(response){
		 				$('#replace').html(response);
		 			}
		});

}


$("#insert").click(function() {
  $( ".d1").toggle();
});


$("#update").click(function() {
  $( ".d2").toggle();
});


$("#delete").click(function() {
  $( ".d3").toggle();
});

$("#view").click(function() {
  $( ".d4").toggle();
});


$(".inner").click(function(e){
    var option = {'id':e.target.id}
    $.ajax({
		async:true,
		type: "POST",
		url: "/select", //name of python method
		data: option,
		success: function(response){
		 				$('#replace').html(response);
		 			}
		});
});


function ins(){
	var params = [$("#did")[0].value,$("#name")[0].value, $("#age")[0].value,$("#gender")[0].value,$("#phone")[0].value]

	// var did = $("#did")[0].value;
	// var name = $("#name")[0].value;
	// var age = $("#age")[0].value;
	// var gender = $("#gender")[0].value;
	// var phone = $("#phone")[0].value;
	for (var i = params.length - 1; i >= 0; i--) {
		if(params[i] == "")
			params[i] = "NULL";
	}
	// send("ins",[did,name,age,gender,phone]);
	send("ins",params)

}

function send(query,params){


	var qtype,d;
	qtype = "/insert";
	d = {
		'username': loginglobal.username,
		'password': loginglobal.password,
		'did':params[0],
		'name':params[1],
		'age':params[2],
		'gender':params[3],
		'phone':params[4]
		};
	
	$.ajax({
		type: "POST",
		url: qtype,
		data: d,
	});
}

