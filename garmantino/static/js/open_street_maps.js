function shopMarkerMap() {
    map = new OpenLayers.Map("map");
    map.addLayer(new OpenLayers.Layer.OSM());

    var lonLat = new OpenLayers.LonLat(27.4335418, 53.89495)
          .transform(
            new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
            map.getProjectionObject() // to Spherical Mercator Projection
          );

    var zoom = 17;

    var markers = new OpenLayers.Layer.Markers( "Markers" );
    map.addLayer(markers);

    var size = new OpenLayers.Size(25, 30); //размер картинки для маркера
    var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h); //смещение картинки для маркера

    var icon = new OpenLayers.Icon(shop_icon_path, size, offset);
    markers.addMarker(new OpenLayers.Marker(lonLat, icon));

    map.setCenter (lonLat, zoom);
}

shopMarkerMap();