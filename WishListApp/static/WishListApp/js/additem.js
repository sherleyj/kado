window.onload = function (){
	var modal = document.getElementsByClassName("add-item-modal")[0];
	var imgs = document.getElementsByClassName("page-img");
	var span = document.getElementsByClassName("close")[0];
	var modal_image = modal.getElementsByTagName("img")[0];
	var i;
	var images_string = ""

	for(i = 0; i< 200; i++){
		images_string += images[i];
	}
	alert(images_string)

	for(i = 0; i < imgs.length; i++) {
	// open modal when user clicks on button
		imgs[i].onclick = function() {
			modal.style.display = "block";
			// var selected_img = imgs[i].getElementsByTagName("img")[0];
			// alert("hi");
			modal_image.src = images[i];
		}
	}

	// close modal when user clicks on x
	span.onclick = function() {
		modal.style.display = "none";
	}

	// close modal when user click outside modal
	window.onclick = function(event){
		if(event.target == modal){
			modal.style.display = "none";
		}
	}

	var test = document.getElementById("test");
	test.onclick = function() {
		alert(selected_img);
	}
}