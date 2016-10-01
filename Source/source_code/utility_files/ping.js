function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(StorePosition);
    } else {
        alert("Error in getting location.");
    }
}

function StorePosition(position){
  location={'latitude':position.coords.latitude , 'longitude':position.coords.longitude}
  updateLocation(location);
}
function updateLocation(location){
    var data =location ;
    $.post(URL, data, function(response){
        if(response === 'success')
        else{ alert('Error! :('); }
      }
};
function ping(){
  while true {
    getLocation();
    sleep(30000);
  }
}
