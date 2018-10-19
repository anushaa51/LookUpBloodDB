var loginglobal;

function login(){
	var login = {'username':$("#username")[0].value, //get username and password values from webpage via its id and create login object
				 'password':$("#password")[0].value
				};
	window.loginglobal = login; //global object to store login details throughout session

	$.ajax({
		async:true,
		type: "POST",
		url: "/login", //name of python method
		data: login,
		success: function(response){
		 				$('#replace').html(response); //replace html id 'response'
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


$(".inner").click(function(e){ //which dropdown option selected
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


function insdonor(){ 
	var params = [$("#did")[0].value,$("#name")[0].value, $("#age")[0].value,$("#gender")[0].value,$("#phone")[0].value]
	send("insdonor",params)

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

function del(){
	$.ajax({
		type: "POST",
		url: "/display",
		success: function(response){
		 				$('body').html(response); //replace html id 'response'
		 			}
	});
}