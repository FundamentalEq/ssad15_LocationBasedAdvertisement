console.log("i was here") ;
console.log("i was here") ;
time_len = 10000;
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(updateLocation);
    } else {
        alert("Error in getting location.");
    }
};
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
};

function updateLocation(position){
    // location={'latitude':position.coords.latitude , 'longitude':position.coords.longitude}
    // console.log(location);
    console.log("i am me") ;
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
            window.time_len = parseInt(ret.time_len)*1000 ;
            // alert(window.time_len) ;
            console.log("time len is ",window.time_len) ;
            console.log("the length of this video is ",time_len) ;
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


function show_ad()
{
    getLocation() ;
    console.log(window.time_len) ;
    setTimeout(show_ad,window.time_len) ;
} ;

$(document).ready( function ping(){
  console.log("i was here") ;
  show_ad() ;
  // setInterval(function(){  console.log(window.time_len) ; getLocation();},window.time_len);
});
