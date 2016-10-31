function get_slots() {
  r=document.getElementById("id_no_of_repeats").value;
  t=document.getElementById("id_time_of_advertisement").value;
  slots=(r*t)/30;
  slot_allowed=Math.ceil(slots);
  document.getElementById("id_no_of_slots").value=slot_allowed;
  document.getElementById("id_no_of_slots").readOnly = true;
}
$(document.getElementById("id_no_of_repeats")).change( function(){
  get_slots();
});
$(document.getElementById("id_time_of_advertisement")).change( function(){
  get_slots();
});
