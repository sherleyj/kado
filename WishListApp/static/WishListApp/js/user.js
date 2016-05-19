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

	$(window).resize(menu_resize);
	menu_resize();

	$(".button-edit").click(function(){
		$(".modal").css("display", "block");
	})

	$(".close").click(function(){
		$(".modal").css("display", "none");
	})

	// $(window).click(function(){

	// })

});
