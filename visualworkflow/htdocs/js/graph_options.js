/* 
 * This script reloads the graph image when one of its display options is changed.
 */

jQuery(document).ready(function($) {
  
  // save the base url of the image for use when updating the source url inside the change event
  $("#graph").data("src", $("#graph").attr("src"));
  $(".graph_option").change(function() {
    var params = new Array();
    
    // add time as a parameter so the browser doesn't cache out of date images
    params.push("time=" + new Date().getUTCMilliseconds());
    
    if ($("#ops").attr("checked"))
      params.push($("#ops").attr("value") + "=1");
    if ($("#perms").attr("checked"))
      params.push($("#perms").attr("value") + "=1");
    $("#graph").attr("src", $("#graph").data("src") + "?" + params.join("&amp;"));
  }).change();
});
