$(document).ready(function(){
	var menu_resize = function(){
		var wl_width = $(".wishlist").width();
		var wl_item_width = $(".wishlist-items").outerWidth(true);
		if (wl_width % wl_item_width == 0) {
			wl_item_width++;
		}
		var new_menu_width = (Math.floor(wl_width/wl_item_width)*wl_item_width); 
		$(".menu").css("width", new_menu_width );	
	}

	$(window).resize(menu_resize);
	menu_resize();
});