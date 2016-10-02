console.log("i was here") ;
console.log("i was here") ;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(updateLocation);
    } else {
        alert("Error in getting location.");
    }
};

function updateLocation(position){
    // location={'latitude':position.coords.latitude , 'longitude':position.coords.longitude}
    // console.log(location);
    console.log("i am me")
    $.ajax({
            type: "POST",
            url: "/ssad15/display_advertisement/",  // URL to your view that serves new info
            data: {
            latitude:position.coords.latitude ,
            longitude:position.coords.longitude,
            csrfmiddlewaretoken: token,
        },
        success : function(ret){
            // alert(ret);
            // alert(ret.path);
            console.log("i am being called again") ;
            console.log(document.getElementById('my_video').src) ;
            document.getElementById('my_video').src = ret.path;
            document.getElementById('my_video1').src = ret.path ;
            console.log(document.getElementById('my_video').src) ;

        },
        error : function(xhr, errmsg,err){
            alert(errmsg);
            alert(xhr.responseText);
        }
    });
        /*.done(function(response) {
          $('#video').append(response);
        });*/
};



$(document).ready( function ping(){
  console.log("i was here") ;
  setInterval(getLocation(),30000);
});
