/**
 * Created by lenovo on 28.09.2016.
 */
function myMap() {
    var shopCoordinates = {lat: 53.91705, lng: 27.45393};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: shopCoordinates
    });
    var marker = new google.maps.Marker({
        position: shopCoordinates,
        map: map,
        title: "Garmantino",
        icon: image
    });
}