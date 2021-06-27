// Mobile navbar
$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
});


// // Close Flash messages
// $("#close-message").on("click", closeFlash);

// function closeFlash(){
//     $("#flash-message").css("display", "none");
//     return false;
// }


$(document).ready( function() {
    setTimeout(function () {
        $("#flash-message")
            .animate({
                'opacity': 0
            }, 750); //you can set a speed just like fadeOut() or fadeIn()
    },5000);

    // $("#div").hover(function(){
    //     $("#div").css("opacity","1");
    // },function(){
    //     $("#div").css("opacity","0");
    // });

});