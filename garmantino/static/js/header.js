/**
 * Created by lenovo on 01.10.2016.
 */
var small_logo = document.getElementById("logo");

small_logo.addEventListener("mouseover", function( event ){
    small_logo.src = logo_red_url;
});

small_logo.addEventListener("mouseout", function( event ){
    small_logo.src = logo_gray_url;
});