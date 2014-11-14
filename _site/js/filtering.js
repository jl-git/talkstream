$(document).ready(function() {
  $(".blurb").toggle();
  $(".toggler").click(function() {
    $(this).parent().next().next().toggle();
    $(this).children(":first").toggleClass("fa-plus-square");
    $(this).children(":first").toggleClass("fa-minus-square");
  });
  $("#button-all").click(function() {
    $(".series-cornell-scan").show();$(".series-cornell-cam").show();$(".series-ucb-lapack").show();$(".series-stanford-la-opt").show();$(".series-mit-amc").show();$(".series-temple-am").show();$(".series-vt-am-colloq").show();$(".series-ncsu-nas").show();$(".series-ncsu-amc").show();$(".series-oxford-nas").show();$(".series-manchester-nas").show();
    $(".series-").show();
  });
  
  $("#button-Cornell").click(function() {
    $(".series-cornell-scan").show();$(".series-cornell-cam").show();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-Berkeley").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").show();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-Stanford").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").show();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-MIT").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").show();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-Temple").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").show();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-VA Tech").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").show();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-NCSU").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").show();$(".series-ncsu-amc").show();$(".series-oxford-nas").hide();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-Oxford").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").show();$(".series-manchester-nas").hide();
    $(".series-").hide();
  });
  
  $("#button-Manchester").click(function() {
    $(".series-cornell-scan").hide();$(".series-cornell-cam").hide();$(".series-ucb-lapack").hide();$(".series-stanford-la-opt").hide();$(".series-mit-amc").hide();$(".series-temple-am").hide();$(".series-vt-am-colloq").hide();$(".series-ncsu-nas").hide();$(".series-ncsu-amc").hide();$(".series-oxford-nas").hide();$(".series-manchester-nas").show();
    $(".series-").hide();
  });
  
});
