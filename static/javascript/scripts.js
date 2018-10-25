var loginglobal;
var row_id = 1;


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
	var did = $("#did")[0].value;
	var bid = $("#bid")[0].value;
	var pdonor = [$("#did")[0].value,$("#name")[0].value, $("#age")[0].value,$("#gender")[0].value,$("#bg")[0].value,$("#phone")[0].value,$("#weight")[0].value] //
	var blood = [$("#bid")[0].value,$("#haemo")[0].value,$("#wbc")[0].value,$("#rbc")[0].value,$("#pc")[0].value,$("#date")[0].value]
	var orgb = [$("#oid")[0].value,$("#brid")[0].value]
	send("insdonor",pdonor,blood,orgb)

}



function send(query,pdonor,blood,orgb){
	var qtype,d;

	if(query==="insdonor"){
		qtype = "/insert";
		d = {
			'username': loginglobal.username,
			'password': loginglobal.password,
			'did':pdonor[0],
			'name':pdonor[1],
			'age':pdonor[2],
			'gender':pdonor[3],
			'bg':pdonor[4],
			'phone':pdonor[5],
			'weight':pdonor[6],
			'bid':blood[0],
			'haemo':blood[1],
			'wbc':blood[2],
			'rbc':blood[3],
			'pc':blood[4],
			'date':blood[5],
			'oid':orgb[0],
			'brid':orgb[1]
			};
		}
	
	if(query==="del"){
		qtype = "/dele";
		console.log("2",pdonor);
		d = {
			'username': loginglobal.username,
			'password': loginglobal.password,			
			'bid':pdonor
		};
	}
	$.ajax({
		type: "POST",
		url: qtype,
		data: d,
	});
}

function viewallblood(){
	$.ajax({
		type: "POST",
		url: "/viewallblood",
		success: function(response){
		 				$('#replace').html(response); //replace html id 'response'
		 			}
	});
}
function viewallorg(){
	$.ajax({
		type: "POST",
		url: "/viewallorg",
		success: function(response){
		 				$('#replace').html(response); //replace html id 'response'
		 			}
	});
}

function viewanorg(){
	d = {
		'oid':$("#oid")[0].value
	};
	$.ajax({
		type: "POST",
		url: "/viewanorg",
		data: d,
		success: function(response){
		 				$('#replace').html(response); //replace html id 'response'
		 			}
	});

}

function viewbybg(){
	d = {
		'bg': $("#bg")[0].value,
		'hid': $("#hid")[0].value
	};
	$.ajax({
		type: "POST",
		url: "/viewbybg",
		data: d,
		success: function(response){
		 				$('#replace').html(response); //replace html id 'response'
		 			}
	});
}

function upddonor(id){
	if(id == 'updname'){
		console.log($("#name")[0].value,$("#did1")[0].value)
		d = {
			'type': "name",
			'name':$("#name")[0].value,
			'did':$("#did1")[0].value
		};
	}
	else if(id == 'updphone')
		d = {
			'type': "phone",
			'phone':$("#phone")[0].value,
			'did':$("#did2")[0].value
		};
	else if(id == 'updweight')
		d = {
			'type': "weight",
			'weight':$("#weight")[0].value,
			'did':$("#did3")[0].value
		};
	else if(id == 'org')
		d = {
			'type': "org",
			'oid':$("#oid")[0].value,
			'brid':$("#brid")[0].value,
			'phone':$("#phone")[0].value

		};

	$.ajax({
		type: "POST",
		url: "/upddonor",
		data: d
		// success: function(response){
		//  				$('#replace').html(response); //replace html id 'response'

		// }
	});
}

// function handleClick(event) {
//   var node = event.target;
//   if (node.name == 'edit') {
//     node.value = "Modify";
//   }
// }

function dele(id){
	var bid = $('#' + id).children('td:first').text();
	$('#' + id).fadeOut('slow', function(here){ 
            $(this).remove();                    
        });    
	console.log("1",bid);
	send("del",bid,null,null);
}


function addRow() {
	$( "tr" ).each(function( row_id ) {
  	 $( this ).attr("id",row_id++);
  	 $(this).attr("ondblclick","dele(this.id)")
	});
}	
