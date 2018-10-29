var login;
var loginglobal;
var row_id = 1;

function wlogin(id){
	

		if(id == "login") {
			if($("#username")[0].value == '' || $("#password")[0].value == '') {
				fieldBlank();
				}

			else {
				window.login = {'username':$("#username")[0].value, //get username and password values from webpage via its id and create login object
					 	'password':$("#password")[0].value
						};
			window.loginglobal = login; //global object to store login details throughout session
			loginajax();
			}
		}
	
		else if(id == "home"){
			window.login = {'username' :loginglobal.username,
						 'password' :loginglobal.password
						};
			loginajax();

		}
}
	

function clicky(id) { //which dropdown option selected
    var option = {'id':id};
    $.ajax({
		async:true,
		type: "POST",
		url: "/select", //python method rendering respective option among insert/delete/update/view
		data: option,
		success: function(response){
		 				$('#replace').html(response);
		 	}
	});
}


function orgbranchdel(id){
	if(id == "orgdel") {
		var d = {
			'type':'org',
			'oid':$("#oid")[0].value
		};		
	}
	else if(id == "branchdel"){
		var d = {
			'type':'branch',
			'oid':$("#oid")[0].value,
			'brid':$("#brid")[0].value
		};
	}

	$.ajax({
		type: "POST",
		url: "/orgbranchdel", //name of python method
		data: d,
		success: function(data){
				if(data['row'] > 0){
					$('#modalhead').html("Congrats!");
					$('#modalbody').html(data['res'] + data['row']);
					if($('.modal-header').hasClass("bg-danger") == true) 
						$('.modal-header').removeClass("bg-danger");

					$('.modal-header').addClass("bg-success");
					$('#mymodal').modal();
				}
				else if(data['row'] == 0){
					oopsError("foreign");
				}
		},
		error: function (){
			oopsError("error");
		}
	});
	
}


function insdonor(id){ 
	if(id=="new"){
		var pdonor = [$("#did")[0].value,$("#name")[0].value, $("#age")[0].value,$("#gender")[0].value,$("#bg")[0].value,$("#phone")[0].value,$("#weight")[0].value] //
		var blood = [$("#bid")[0].value,$("#haemo")[0].value,$("#wbc")[0].value,$("#rbc")[0].value,$("#pc")[0].value,$("#date")[0].value]
		var orgb = [$("#oid")[0].value,$("#brid")[0].value]
		var arraycheck = [pdonor,blood,orgb]
		var blank = checkBlank(arraycheck);
		if(blank!=1)
			send("insnew",pdonor,blood,orgb)
	}
	
	else if(id == "old"){
		var blood = [$("#did1")[0].value,$("#bid1")[0].value,$("#haemo1")[0].value,$("#wbc1")[0].value,$("#rbc1")[0].value,$("#pc1")[0].value,$("#date1")[0].value]
		var orgb = [$("#oid1")[0].value,$("#brid1")[0].value]
		var arraycheck = [blood,orgb]
		var blank = checkBlank(arraycheck);
		if(blank!=1)
			send("insold",null,blood,orgb)
	}
}


function insorg(id){
	if(id=="neworg"){
		var org = [$("#oid")[0].value,$("#oname")[0].value,$("#no")[0].value]
		var branch = [$("#brid")[0].value,$("#braddr")[0].value,$("#brphno")[0].value]
		var distance = [$("#hid1")[0].value,$("#hid2")[0].value,$("#hid3")[0].value]
		var arraycheck = [org,branch,distance]
		var blank = checkBlank(arraycheck);
		if(blank!=1)
			send("neworg",org,branch,distance)
		}
	else if(id == "oldorg"){
		var branch = [$("#brid1")[0].value,$("#braddr1")[0].value,$("#brphno1")[0].value,$("#oid1")[0].value]
		var distance = [$("#ohid1")[0].value,$("#ohid2")[0].value,$("#ohid3")[0].value]		
		var arraycheck = [branch,distance]
		var blank = checkBlank(arraycheck);
		if(blank!=1)
			send("oldorg",null,branch,distance)
		}

	}


function send(query,pdonor,blood,orgb){
	var qtype,d;

	if(query=="insnew"){
		qtype = "/insert";
		d = {
			'type':"insnew",
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
	else if(query=="insold"){
		qtype = "/insert";
		d = {
			'type': "insold",
			'username': loginglobal.username,
			'password': loginglobal.password,
			'did':blood[0],
			'bid':blood[1],
			'haemo':blood[2],
			'wbc':blood[3],
			'rbc':blood[4],
			'pc':blood[5],
			'date':blood[6],
			'oid':orgb[0],
			'brid':orgb[1]
			};
		}
	else if(query == "neworg"){
		qtype = "/insertorg";
		d = {
			'type':"neworg",
			'username' : loginglobal.username,
			'password': loginglobal.password,
			'oid':pdonor[0],
			'oname':pdonor[1],
			'no':pdonor[2],
			'brid':blood[0],
			'braddr':blood[1],
			'brphno':blood[2],
			'hid1':orgb[0],
			'hid2':orgb[1],
			'hid3':orgb[2]

		};
	}

	else if(query == "oldorg"){
		qtype = "/insertbranch";
		d = {
			'type':"oldorg",
			'username' : loginglobal.username,
			'password': loginglobal.password,
			'oid':blood[3],
			'brid':blood[0],
			'braddr':blood[1],
			'brphno':blood[2],
			'hid1':orgb[0],
			'hid2':orgb[1],
			'hid3':orgb[2]

		};
	}
	
	else if(query==="del"){
		qtype = "/dele";
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
		success: function(data){
			if(data['res']=="SUCC"){

				$('#modalhead').html("Congrats!" );
				$('#modalbody').html("Insert was successful!");
				if($('.modal-header').hasClass("bg-danger") == true) 
					$('.modal-header').removeClass("bg-danger");
				$('.modal-header').addClass("bg-success");
				$('#mymodal').modal();
			}
			else if(data['res']=="PRI"){
				oopsError("primary");
			}

			else if(data['res']=="FOR"){
				oopsError("foreign");
			}
			else if(data['res']=="UNK"){
				oopsError("error");
			}
		 },
		error: function (){
			oopsError("error");
			}
		});
}


function navcheck(id){
	if(id=="NewNavbtn") {
		if($('#OldNav').hasClass("show") == true) 
			$('#OldNav').removeClass("show");
			$('OldNavbtn').addClass("collapsed")
		}
	else if(id =="OldNavbtn") {
		if($('#NewNav').hasClass("show") == true) 
			$('#NewNav').removeClass("show");
			$('NewNavbtn').addClass("collapsed")
	}
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

	else if(id == 'orgname')
		d = {
			'type': "orgname",
			'oid':$("#oid1")[0].value,
			'name':$("#name")[0].value,

		};

	$.ajax({
		type: "POST",
		url: "/upddonor",
		data: d,
			success: function(data){
				if(data['row'] > 0){
					$('#modalhead').html("Congrats!");
					$('#modalbody').html(data['res'] + data['row']);
					if($('.modal-header').hasClass("bg-danger") == true) 
						$('.modal-header').removeClass("bg-danger");
					$('.modal-header').addClass("bg-success");
					$('#mymodal').modal();
				}
				else if(data['row'] == 0){
					oopsError("foreign")
				}
		},
			error: function (){
				oopsError("error");
		}
	});
}


function dele(id){
	var bid = $('#' + id).children('td:first').text();
	if(id != 0) {
		$('#' + id).fadeOut('slow', function(here){ 
            $(this).remove();                    
        });    
	}
	send("del",bid,null,null);
}


function addRow() {
	$( "tr" ).each(function( row_id ) {
  	 $( this ).attr("id",row_id++);
  	 $(this).attr("ondblclick","dele(this.id)")
	});
}	


function fieldBlank(){
	$('#modalhead').html("Oops!");
	$('#modalbody').html("Some field was left blank, please fill in!");
	$('.modal-header').addClass("bg-warning");
	$('#mymodal').modal();
}


function loginajax(){
	$.ajax({
				async:true,
				type: "POST",
				url: "/login", //name of python method
				data: login,
				success: function(response){
				 				$('body').html(response); //replace html id 'response'
				 }
		});
}


function checkBlank(arraycheck){
	var blank = 0;
	for (var i = 0 ; i <arraycheck.length ; i++) {
		var element = arraycheck[i];
		for(var j = 0; j < element.length; j++){
			if(element[j] == ""){
				fieldBlank();
				blank=1;
				break;
			}
		}
		if(blank==1) break;
	}
	if(blank!=1)
		$('.modal-header').removeClass("bg-warning");
	return blank;
}


function oopsError(type){
	$('#modalhead').html("Oops!");
	if($('.modal-header').hasClass("bg-success") == true) 
		$('.modal-header').removeClass("bg-success");
	$('.modal-header').addClass("bg-danger");
	if (type == "foreign")
		$('#modalbody').html(" That entry does not exist!");
	else if(type == "primary")
		$('#modalbody').html(" That entry already exists!");
	else	
		$('#modalbody').html(" There was an error!");
	$('#mymodal').modal();
}
