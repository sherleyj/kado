window.onload = function (){
	var menu = document.getElementsByClassName("menu")[0];	
	var wl = document.getElementsByClassName("wishlist")[0];
	var wl_width = wl.offsetWidth;
	var wl_item = document.getElementsByClassName("wishlist-items")[0];
	var wl_item_margin = wl_item.style.margin;

	var wl_item_width = wl_item.offsetWidth + 5*2;
	var num_wl_item = Math.floor(wl_width/wl_item_width);
	if(wl_width%wl_item_width == 0){
		num_wl_item--;
	}
	menu.style.width = (wl_item_width*num_wl_item - (5*2)) + "px";

	// wl.onchange = function(){
	// 	var wl_item_width = wl_item.offsetWidth + 5*2;
	// 	var num_wl_item = Math.floor(wl_width/wl_item_width);
	// 	if(wl_width%wl_item_width == 0){
	// 	num_wl_item--;
	// }
	// menu.style.width = (wl_item_width*num_wl_item - (5*2)) + "px";

	// }

	console.log("wl width: " + wl_width);
	console.log("wl_item_width: " + wl_item_width);
	console.log("num_wl_item: " + num_wl_item);
	console.log("menu width: " + menu.style.width);
	console.log("wl margin: " + wl_item_margin);
}

