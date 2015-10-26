"use strict"

var i = 0, lastNumber = 0, paths, n,
    img = document.getElementById("image-slider"),
    buttonLeft = document.getElementById("button-left"),
    buttonRight = document.getElementById("button-right");
    
    paths = ["../imgs/item/itemPhoto1.png",
             "../imgs/item/itemPhoto2.png",
             "../imgs/item/itemPhoto3.png",
             "../imgs/item/itemPhoto4.jpg",
             "../imgs/item/itemPhoto5.png",];
    n = paths.length;

var buttonLeftClick = function(){
    console.log(lastNumber, img.src);
    if (lastNumber != 0) img.src = paths[--lastNumber];
    else{
        lastNumber = n-1;
        img.src = paths[lastNumber];
    }
};

var buttonRightClick = function(){
    console.log(lastNumber, img.src);
    if (lastNumber != n-1) img.src = paths[++lastNumber];
    else{
        lastNumber = 0;
        img.src = paths[lastNumber];
    }
};

buttonLeft.addEventListener("click", buttonLeftClick);
buttonRight.addEventListener("click", buttonRightClick);