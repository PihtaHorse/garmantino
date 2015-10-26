"use strict"
/*
var buttonToTop = document.querySelector(".move-up .fa-angle-up");
buttonToTop.addEventListener("click", function(){window.scrollTo(0, 0)});

var i, n, last, lastNumber,
    bigImg = document.querySelector("#mainImgWrapper"),
    buttonUp = document.querySelector("#buttonPrevious"),
    buttonDown = document.querySelector("#buttonNext"), 
    imgs = document.querySelectorAll("#smallImages .smallImg"),
    imgWrappers = document.querySelectorAll("#smallImages .smallImgWrapper");

n = imgs.length;

var smallImgClick = function(smallImg, i){
    var callback = function(){
            bigImg.style.backgroundImage = "url(" + smallImg.src + ")";
            last.style.opacity = 0.4;
            smallImg.style.opacity = 1;
            last = smallImg;
            lastNumber = i;
        };
    
    return callback;
};

var buttonUpClick = function(){
    console.log(last.src, lastNumber);
    if (lastNumber != 0) {
        last.style.opacity = 0.4;
        last = imgs[--lastNumber];
        last.style.opacity = 1;
        bigImg.style.backgroundImage = "url(" + last.src + ")";
    };
    console.log(last.src, lastNumber);
};

var buttonDownClick = function(){
    console.log(last.src, lastNumber);
    if (lastNumber != n-1) {
        last.style.opacity = 0.4;
        last = imgs[++lastNumber];
        last.style.opacity = 1;
        bigImg.style.backgroundImage = "url(" + last.src + ")";
    };
    console.log(last.src, lastNumber);
};

buttonUp.addEventListener("click", buttonUpClick);
buttonDown.addEventListener("click", buttonDownClick);

for(i = 0; i < n; i++ ){
    imgs[i].style.opacity = 0.4;
    imgs[i].addEventListener("click", smallImgClick(imgs[i], i));
}

lastNumber = 0;
if (n != 0){
    last = imgs[0];
    imgs[0].style.opacity = 1;
}
*/