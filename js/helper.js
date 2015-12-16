function AnimateRotate(angle, selector) {
    // caching the object for performance reasons
    // we use a pseudo object for the animation
    // (starts from `0` to `angle`), you can name it as you want
    $elem = $(selector);

    $elem.animate({deg: angle}, {
        duration: 600,
        step: function(now) {
            $elem.css({'transform': 'rotate(' + now + 'deg)'});
            $elem.css({'-ms-transform': 'rotate(' + now + ')deg'});
            $elem.css({'-webkit-transform': 'rotate(' + now + ')deg'});
        }
    });
}

function getCookie(cname) {
var name = cname + "=";
var ca = document.cookie.split(';');
for(var i=0; i<ca.length; i++) {
  var c = ca[i];
  while (c.charAt(0)==' ') c = c.substring(1);
    if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
  }
  return "";
}

function showHelp() {
  $('#light').fadeIn("slow");
  $('#fade').fadeIn("slow");
}

function hideHelp() {
  $('#light').fadeOut("slow");
  $('#fade').fadeOut("slow");
}