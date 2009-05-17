(function($){
  window.addLink = function(elm) {
    var link = document.createElement("a");
    link.setAttribute("href", "javascript:window.fondleTabs($('#" + $(elm).attr("id") + " a'))");
    link.innerHTML = $(elm).text();
    $(elm).empty().append(link);
  }
  
  window.fondleTabs = function(elm) {
    
    // make previously active tabs inactive and make this tab active
    $("#editor_tabs li.active").removeClass("active");
    $(elm).parent().addClass("active");
    
    // hide all active panels and unhide the panel that corresponds with this tab
    $("#editor_tabcontent div.active").removeClass("active").addClass("inactive");
    $("#content_" + $(elm).parent().attr("id").split("_")[1]).removeClass("active").addClass("active");
    
    // add links to the inactive tabs and remove the link from the newly active tab
    $("#editor_tabs li[class!=active]").each(function() { addLink(this) });
    $(elm).replaceWith($(elm).text());
  }
})(jQuery);
