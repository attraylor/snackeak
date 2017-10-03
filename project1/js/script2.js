$(document).ready(function(){
	$("form#main_input_box1").submit(function(event){
		event.preventDefault();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		var checkBox = "<div class='checkbox'><label><input type='checkbox' class='pull-right'></label></div>";
		$(".list_of_items1").append("<li class='list-group-item'>" + "<div class='text_holder'>" + $("#custom_textbox").val() +"  DUE:" + $("#custom_textbox2").val() + twoButtons + "</div>" + checkBox + "</li>");
		$("#custom_textbox").val('');
		$("#custom_textbox2").val('');
	});
	

	$(".list_of_items1").on("click", "button.delete", function(){
		$(this).closest("li").remove();
	});

	$(".list_of_items1").on("click", "button.edit", function (){
		var editItemBox = "<form class='edit_input_box'><input type='text' class='itembox'></form>";
		var originalItem = $(this).parent().val();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		$(this).closest("div.text_holder").replaceWith(editItemBox);
		$("form.edit_input_box ").on("submit", function(){
			event.preventDefault(); 
			var checkBox = "<label><input type='checkbox'></label>";
			$(this).replaceWith("<div>" + $(".itembox").val() + twoButtons + "</div>");
		}); 
	});
	
	$(".list_of_items1").on("click", ":checkbox", function (){
		$(this).closest("li").toggleClass("completed_item");
	});
	
	
	
	$("form#main_input_box2").submit(function(event){
		event.preventDefault();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		var checkBox = "<div class='checkbox'><label><input type='checkbox' class='pull-right'></label></div>";
		$(".list_of_items2").append("<li class='list-group-item'>" + "<div class='text_holder'>" + $("#custom_textbox3").val() +"  DUE:" + $("#custom_textbox4").val() + twoButtons + "</div>" + checkBox + "</li>");
		$("#custom_textbox3").val('');
		$("#custom_textbox4").val('');
	});
	

	$(".list_of_items2").on("click", "button.delete", function(){
		$(this).closest("li").remove();
	});

	$(".list_of_items2").on("click", "button.edit", function (){
		var editItemBox = "<form class='edit_input_box'><input type='text' class='itembox'></form>";
		var originalItem = $(this).parent().val();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		$(this).closest("div.text_holder").replaceWith(editItemBox);
		$("form.edit_input_box ").on("submit", function(){
			event.preventDefault(); 
			var checkBox = "<label><input type='checkbox'></label>";
			$(this).replaceWith("<div>" + $(".itembox").val() + twoButtons + "</div>");
		}); 
	});
	
	$(".list_of_items2").on("click", ":checkbox", function (){
		$(this).closest("li").toggleClass("completed_item");
	});
	
	
	
	$("form#main_input_box3").submit(function(event){
		event.preventDefault();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		var checkBox = "<div class='checkbox'><label><input type='checkbox' class='pull-right'></label></div>";
		$(".list_of_items3").append("<li class='list-group-item'>" + "<div class='text_holder'>" + $("#custom_textbox5").val() +"  DUE:" + $("#custom_textbox6").val() + twoButtons + "</div>" + checkBox + "</li>");
		$("#custom_textbox5").val('');
		$("#custom_textbox6").val('');
	});
	

	$(".list_of_items3").on("click", "button.delete", function(){
		$(this).closest("li").remove();
	});

	$(".list_of_items3").on("click", "button.edit", function (){
		var editItemBox = "<form class='edit_input_box'><input type='text' class='itembox'></form>";
		var originalItem = $(this).parent().val();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		$(this).closest("div.text_holder").replaceWith(editItemBox);
		$("form.edit_input_box ").on("submit", function(){
			event.preventDefault(); 
			var checkBox = "<label><input type='checkbox'></label>";
			$(this).replaceWith("<div>" + $(".itembox").val() + twoButtons + "</div>");
		}); 
	});
	
	$(".list_of_items3").on("click", ":checkbox", function (){
		$(this).closest("li").toggleClass("completed_item");
	});
	
	
	$("form#main_input_box4").submit(function(event){
		event.preventDefault();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		var checkBox = "<div class='checkbox'><label><input type='checkbox' class='pull-right'></label></div>";
		$(".list_of_items4").append("<li class='list-group-item'>" + "<div class='text_holder'>" + $("#custom_textbox7").val() +"  DUE:" + $("#custom_textbox8").val() + twoButtons + "</div>" + checkBox + "</li>");
		$("#custom_textbox7").val('');
		$("#custom_textbox8").val('');
	});
	

	$(".list_of_items4").on("click", "button.delete", function(){
		$(this).closest("li").remove();
	});

	$(".list_of_items4").on("click", "button.edit", function (){
		var editItemBox = "<form class='edit_input_box'><input type='text' class='itembox'></form>";
		var originalItem = $(this).parent().val();
		var deleteButton = "<button class='delete btn btn-warning'>Delete</button>";
		var editButton = "<button class='edit btn btn-success'>Edit</button>";
		var twoButtons = "<div class='btn-group pull-right'>" + deleteButton + editButton + "</div>";
		$(this).closest("div.text_holder").replaceWith(editItemBox);
		$("form.edit_input_box ").on("submit", function(){
			event.preventDefault(); 
			var checkBox = "<label><input type='checkbox'></label>";
			$(this).replaceWith("<div>" + $(".itembox").val() + twoButtons + "</div>");
		}); 
	});
	
	$(".list_of_items4").on("click", ":checkbox", function (){
		$(this).closest("li").toggleClass("completed_item");
	});
	
});



