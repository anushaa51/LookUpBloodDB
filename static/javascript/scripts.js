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

	if(query==="insdonor"){
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
		}
	
	if(query==="del"){
		qtype = "/dele";
		d = {
			'username': loginglobal.username,
			'password': loginglobal.password,			
			'cond':params
		};
	}
	$.ajax({
		type: "POST",
		url: qtype,
		data: d,
	});
}

function viewdonor(){
	$.ajax({
		type: "POST",
		url: "/viewdonor",
		success: function(response){
		 				$('body').html(response); //replace html id 'response'
		 			}
	});
}

// function handleClick(event) {
//   var node = event.target;
//   if (node.name == 'edit') {
//     node.value = "Modify";
//   }
// }

function dele(id){
	var cond = Number($('#' + id).children('td:first').text());
	$('#' + id).fadeOut('slow', function(here){ 
            $(this).remove();                    
        });    
	
	send("del",cond);
}

var row_id = 1;

function addRow() {
	$( "tr" ).each(function( row_id ) {
  	 $( this ).attr("id",row_id++);
  	 $(this).attr("ondblclick","dele(this.id)")
	});
}	

