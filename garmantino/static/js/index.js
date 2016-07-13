"use strict";
var imgs, links, i, n, repeatFunction, repeatFunctionCalls;

imgs = document.querySelectorAll("a > img");
links = document.querySelectorAll("div .hexagon-part2 > a");
n = imgs.length;
repeatFunctionCalls = 1;

repeatFunction = function(img, a, i){
    a.href = item_urls[repeatFunctionCalls % n];
    img.src = photos_urls[repeatFunctionCalls % n];
    repeatFunctionCalls++;
};

for(i = 0; i < n; i++){
    imgs[i].addEventListener("animationiteration", repeatFunction(imgs[i], links[i], i));
}