"use strict"
var imgs, links, i, n, repeatFunction;

imgs = document.querySelectorAll("a > img");
links = document.querySelectorAll("div .hexagon-part2 > a");
n = imgs.length;

repeatFunction = function(img, a, i){
    var fun = function(){
            img.src = "../imgs/pic" + ((fun.calls  + i) % 6 + 3) + ".png";
            a.href = "#" + (i + fun.calls) % 6;
            console.log(fun.calls++);
        };
    fun.calls = 0;
    
    return fun;
};

for(i = 0; i < imgs.length; i++){
    imgs[i].addEventListener("animationiteration", repeatFunction(imgs[i], links[i], i));
};