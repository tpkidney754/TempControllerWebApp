function incTemp(){
	var temp = parseInt(document.getElementById("desiredTemp").value);
	temp++;
	document.getElementById("desiredTemp").value = temp.toString();
}
function decTemp(){
	var temp = parseInt(document.getElementById("desiredTemp").value);
	temp--;
	document.getElementById("desiredTemp").value = temp.toString();
}
function incRange(){
	var range = parseInt(document.getElementById("desiredRange").value);
	range++;
	document.getElementById("desiredRange").value = range.toString();
}
function decRange(){
	var range = parseInt(document.getElementById("desiredRange").value);
	range--;
	document.getElementById("desiredRange").value = range.toString();
}