"use strict"

var popUpWindow = document.getElementById("pop-up");
var popUpBackground = document.getElementById("pop-up-background");
var popUp = document.getElementById("question-form-wrapper");
var form = document.getElementById("question-form");

document.getElementById("ask-question-button").addEventListener("click", function( e ){
    popUpWindow.style.visibility = "visible";
    popUp.style.marginBottom = "0";
    popUpBackground.style.opacity = "0.7";
});

var close_pop_up = function (e) {
    popUpWindow.style.visibility = "hidden";
    popUp.style.marginBottom = "100px";
   popUpBackground.style.opacity = "0";
};

popUpBackground.addEventListener("click", close_pop_up);
document.getElementById("close").addEventListener("click", close_pop_up);


form.addEventListener("submit", function(event){
    var email = form.elements['email'].value;
    var phone = form.elements['phone'].value;
    console.log(email, phone);

    if( !(email || phone)) {
        event.preventDefault();
        var input = document.getElementById("email");
        input.style.boxShadow = "1px 1px 15px red";
    }
});