let modal = document.getElementById("my-modal"); //Popup modal by default HIDDEN
let overlayed = document.getElementById("overlayed") //overlay bg by default HIDDEN
let btn = document.getElementById("open-btn"); //Login btn 
let button = document.getElementById("ok-btn"); //Ok btn
var current_step = 0;
    // We want the modal to open when the Open button is clicked
btn.onclick = function() {
modal.style.display = "block";
overlayed.style.display = "block";
alert("Login")
}
// We want the modal to close when the OK button is clicked
button.onclick = function() {
modal.style.display = "none";
overlayed.style.display = "none";
}
window.onclick = function(event) {
if (event.target == overlayed)  {
    modal.style.display = "none";
    overlayed.style.display = "none";
}}


