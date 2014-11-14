---
---

$(document).ready(function() {
  $(".blurb").toggle();
  $(".toggler").click(function() {
    $(this).parent().next().next().toggle();
    $(this).children(":first").toggleClass("fa-plus-square");
    $(this).children(":first").toggleClass("fa-minus-square");
  });
  $("#button-all").click(function() {
    {% for series in site.data.series_names %}{% assign tag = series[0] %}$(".series-{{ tag }}").show();{% endfor %}
    $(".series-").show();
  });
  {% for filter in site.data.filters %}
  $("#button-{{ filter.name }}").click(function() {
    {% for series in site.data.series_names %}{% assign tag = series[0] %}{% if filter[tag] %}$(".series-{{ tag }}").show();{% else %}$(".series-{{ tag }}").hide();{% endif %}{% endfor %}
    $(".series-").hide();
  });
  {% endfor %}
});
