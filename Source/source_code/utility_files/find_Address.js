function Get(yourUrl){
var Httpreq = new XMLHttpRequest(); // a new request
Httpreq.open("GET",yourUrl,false);
Httpreq.send(null);
return Httpreq.responseText;

    }

function find_address(address)
{
    var reqUrl = "http://nominatim.openstreetmap.org/search/" + address + "?format=json&addressdetails=1&limit=1&polygon_svg=1" ;
    var reqAnswer = Get(reqUrl) ;
    var Answer_json = JSON.parse(reqAnswer) ;
    var longititude = Answer_json[0].lon ;
    var latitude = Answer_json[0].lat ;
}
