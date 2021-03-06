---
---

$(document).ready(function() {

    // Show blurbs on demand
    $(".blurb").hide();
    $(".toggler").click(function(e) {
        e.preventDefault();
        var target = $(this).attr("id");
        $("." + target).toggle()
        $(this).children(":first").toggleClass("fa-plus-square");
        $(this).children(":first").toggleClass("fa-minus-square");
    });
    
    // Implement client-side filtering
    $("#filter-all").addClass("pure-menu-selected");
    $("#filters a").click(function(e) {
        e.preventDefault();
        var filter = $(this).attr("id");
        $(".talk").show();
        $(".talk:not(." + filter + ")").hide();
        $("#filters li").removeClass("pure-menu-selected");
        $(this).parent().addClass("pure-menu-selected");
    });
    
});
