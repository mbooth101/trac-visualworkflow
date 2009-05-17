/* 
 * This script reloads the graph image when one of its display options is changed.
 */

(function($){
  window.reloadGraph = function(elm) {
    var params = new Array();
    
    // add time as a parameter so the browser doesn't cache out of date images
    params.push("time=" + new Date().getTime());
    
    if ($("#ops").attr("checked"))
      params.push($("#ops").attr("value") + "=1");
    if ($("#perms").attr("checked"))
      params.push($("#perms").attr("value") + "=1");
    $("#graph").attr("src", $("#graph").data("src") + "?" + params.join("&amp;"));
  }
})(jQuery);

jQuery(document).ready(function($) {
  
  // save the base url of the image for use when updating the source url inside the change event
  $("#graph").data("src", $("#graph").attr("src"));
  
  // add the change events and call the reload function once on page load, to make
  // sure the options are in sync with the image
  $(".graph_option").change(function() { reloadGraph(this) });
  window.reloadGraph();
});
