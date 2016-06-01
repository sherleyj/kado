

$(document).ready(function(){

	var num_columns_wl = function(){
		var wl_width = $(".wishlist").width();
		var wl_item_width = $(".wishlist-item-empty").outerWidth(true);
		return Math.floor(wl_width/wl_item_width);
	}

	var menu_resize = function(){
		var wl_item_width = $(".wishlist-item-empty").outerWidth(true);
		var new_menu_width = num_columns_wl() * wl_item_width; 
		$(".menu").css("width", new_menu_width );
	}

	var open_modal = function(){
		$(".modal").css("display", "block");
		// console.log($('.item_id').text());
		// console.log($(this).siblings(".hi").text());
		var item_id = $(this).next().text();
		$("#form-edit-item").attr('action', "/submitedititem/" + item_id);

		console.log($("#form-edit-item").attr('action'));
		console.log(item_id);
	}

	var close_modal = function(){
		$(".modal").css("display", "none");
	}

	$(window).resize(menu_resize);
	menu_resize();

	$(".button-edit").click(open_modal);
	$(".button-x").click(close_modal);

	var submit_form = function(){
		alert("Item Updated");
	}

	// $(window).click(function(){})
	// $(".button-remove").click();
});
