window.onload = function (){
	var modal = document.getElementsByClassName("modal")[0];
	var imgs = document.getElementsByClassName("page-img");
	var span = document.getElementsByClassName("close")[0];
	var modal_content = document.getElementsByClassName("modal-content")[0];
	var add_img_input = document.getElementById("input_img_url");
	var i;
	var images_string = ""
	var chosen_image = 0;

	// open modal when user clicks on image
	for(i = 0; i < imgs.length; i++) {
		var img_div = imgs[i]
		img_div.onclick = displayModal;
	}
	function displayModal () {
		modal.style.display = "block";
		modal_content.getElementsByTagName('img')[0].src = this.getElementsByTagName('img')[0].src;
		add_img_input.value = this.getElementsByTagName('img')[0].src;
	}

	// close modal when user clicks on x
	span.onclick = function () {
		modal.style.display = "none";
	}

	// close modal when user click outside modal
	window.onclick = function (event) {
		if(event.target == modal){
			modal.style.display = "none";
		}
	}

	// var test = document.getElementById("test");
	// test.onclick = function() {
	// 	alert(selected_img);
	// }
}