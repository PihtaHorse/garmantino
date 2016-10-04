"use strict";
var animated_hexagons, i, n, animation_duration, animation_delay;
var wrapper = document.getElementsByClassName('hexagons-wrapper')[0];
var oddRow = "'hexagon-row-odd'", evenRow = "'hexagon-row-even'";
var rowsNumber = wrapper.children.length;

if(rowsNumber % 2 == 0) {
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(5, oddRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(5, oddRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(5, oddRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
}
else {
    wrapper.insertAdjacentHTML('beforeend', newRow(5, oddRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(5, oddRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(5, oddRow));
    wrapper.insertAdjacentHTML('beforeend', newRow(6, evenRow));
}


animated_hexagons = document.querySelectorAll(".animated");
n = animated_hexagons.length;
animation_duration = 6.25 * n;

window.onload = setTimeout(function () {
    for (i = 0; i < n; i++) {
        animation_delay = -6.25 * i;
        animated_hexagons[i].style.animationName = 'anim1';
        animated_hexagons[i].style.animationDuration = animation_duration.toString() + 's';
        animated_hexagons[i].style.animationTimingFunction = 'linear';
        animated_hexagons[i].style.animationDelay = animation_delay.toString() + 's';
        animated_hexagons[i].style.animationIterationCount = 'infinite';
    }
}, 2500);

