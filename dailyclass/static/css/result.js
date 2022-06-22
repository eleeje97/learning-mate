window.onload = initall;

function initall(){
    $(".result_content2").hide();
    setTimeout(function () {
    $(".search").fadeOut(400);
    $(".result_content2").fadeIn(4000);
    },2500);
}