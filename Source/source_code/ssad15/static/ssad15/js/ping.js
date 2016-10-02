function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(updateLocation);
    } else {
        alert("Error in getting location.");
    }
}

function updateLocation(position){
    location={'latitude':position.coords.latitude , 'longitude':position.coords.longitude}

    $.ajax({
            type: "GET",
            url: {% url 'display_advertisement' %},  // URL to your view that serves new info
            data: {'latitude':position.coords.latitude , 'longitude':position.coords.longitude}

        })
        .done(function(response) {
          $('#video').append(response);
        });
};
document.getElementById('start').onclick = function ping(){
  setinterval(getLocation(),30000);
}
