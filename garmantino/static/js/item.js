"use strict"

var i = 0, lastNumber = 0,
    img = document.getElementById("slider"),
    buttonLeft = document.getElementById("button-left"),
    buttonRight = document.getElementById("button-right"),
    n = paths.length,
    circles = document.getElementsByClassName("circle"),
    currentCircle = document.getElementsByClassName("current-circle")[0];

if(n <= 1){
    var buttons = document.getElementsByClassName("button");

    for(i=0; i<buttons.length; i++){
        buttons[i].style.borderColor = "transparent";
    }

    circles[0].style.backgroundColor = "transparent";
}
else {
    var buttonLeftClick = function(){

        if (lastNumber != 0) img.src = paths[--lastNumber];
        else{
            lastNumber = n-1;
            img.src = paths[lastNumber];
        }
        currentCircle.classList.remove('current-circle');
        currentCircle = circles[lastNumber];
        currentCircle.classList.add('current-circle');
    };

    var buttonRightClick = function(){
        if (lastNumber != n-1) img.src = paths[++lastNumber];
        else{
            lastNumber = 0;
            img.src = paths[lastNumber];
        }
        currentCircle.classList.remove('current-circle');
        currentCircle = circles[lastNumber];
        currentCircle.classList.add('current-circle');
    };

    buttonLeft.addEventListener("click", buttonLeftClick);
    buttonRight.addEventListener("click", buttonRightClick);
}

for(i=0; i<circles.length; i++){

    var handlerCreator = function (index) {
        return function () {
            currentCircle.classList.remove('current-circle');
            currentCircle = circles[index];
            currentCircle.classList.add('current-circle');

            lastNumber = index;
            img.src = paths[index];
        }
    };

    circles[i].addEventListener("click", handlerCreator(i));
}