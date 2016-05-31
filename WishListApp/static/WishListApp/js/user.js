

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
		$(".item_id_input").val($(this).$("#item_id span").text());
	}

	var close_modal = function(){
		$(".modal").css("display", "none");
	}

	$(window).resize(menu_resize);
	menu_resize();

	$(".button-edit").click(open_modal);
	$(".button-x").click(close_modal);

	// $(window).click(function(){})
	// $(".button-remove").click();
});
