var vectorSource = new ol.source.Vector({
      //create empty vector
    });

    //create a bunch of icons and add to source vector
        var iconFeature = new ol.Feature({geometry: new
            ol.geom.Point(ol.proj.transform([78, 17], 'EPSG:4326',   'EPSG:3857'))
            });
        vectorSource.addFeature(iconFeature);


    //create the style
    var iconStyle = new ol.style.Style({
      image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
        anchor: [0.5, 46],
        anchorXUnits: 'fraction',
        anchorYUnits: 'pixels',
        opacity: 0.75,
        src: 'http://openlayers.org/en/v3.9.0/examples/data/icon.png'
      }))
    });
    //add the feature vector to the layer vector, and apply a style to whole layer
    var vectorLayer = new ol.layer.Vector({
      source: vectorSource,
      style: iconStyle
    });

var map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM() }),vectorLayer
  ],
  target: 'map',
  controls: ol.control.defaults({
    attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
      collapsible: false
    })
  }),
  view: new ol.View({
    center: [0, 0],
    zoom: 2
  })
});
console.log("i was here :P");
map.on('click', function(evt) {
    var lonlat = ol.proj.transform(evt.coordinate, 'EPSG:3857', 'EPSG:4326');
    var lon = lonlat[0];
    var lat = lonlat[1];
    map.getView().setCenter(evt.coordinate) ;
    map.getView().setZoom(map.getView().getZoom()+1) ;
    var iconFeature = new ol.Feature({geometry: new ol.geom.Point(evt.coordinate)});
    vectorSource.clear() ;
    vectorSource.addFeature(iconFeature);
    console.log(lat) ;
    console.log(lon) ;
});

document.getElementById('zoom-out').onclick = function() {
  var view = map.getView();
  var zoom = view.getZoom();
  view.setZoom(zoom - 1);
};

document.getElementById('zoom-in').onclick = function() {
  var view = map.getView();
  var zoom = view.getZoom();
  view.setZoom(zoom + 1);
};
