window.onload = function (){
	

	function menu_resize () {
		var menu = document.getElementsByClassName("menu")[0];	
		var wl = document.getElementsByClassName("wishlist")[0];
		var wl_item = document.getElementsByClassName("wishlist-items")[0];
		var wl_item_style = wl_item.currentStyle || window.getComputedStyle(wl_item);
		var wl_item_margin = wl_item_style.margin;
		var wl_width = wl.offsetWidth;
		var wl_item_width = wl_item.offsetWidth + 5*2;
		var num_wl_item = Math.floor(wl_width/wl_item_width);
		if(wl_width%wl_item_width == 0){
			num_wl_item--;
		}
		menu.style.width = (wl_item_width*num_wl_item - (5*2)) + "px";
		console.log(document.getElementsByClassName("wishlist-items")[0].style.margin);
		console.log(wl_item_margin);
		// console.log(wl_width/wl_item_width);
		// console.log(Math.floor(wl_width/wl_item_width));
	}

	menu_resize();
	window.onresize = menu_resize;
	// document.getElementsByClassName("menu")[0].onresize = menu_resize();
}

