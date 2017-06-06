/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles-js', '/static/particles/particles.json', function() {
  console.log('callback - particles.js config loaded');
});

$(document).ready(function(){
$('.ir-arriba').click(function(){
$('body, html').animate({
scrollTop: '0px'
});
});
$(window).scroll(function(){
if($(this).scrollTop() > 0){
$('.ir-arriba').slideDown(300);
}else{
$('.ir-arriba').slideUp(300);
}
});
});

