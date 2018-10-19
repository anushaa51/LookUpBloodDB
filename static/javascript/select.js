
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