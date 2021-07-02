// Materialize mobile navbar
$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
});


// // Close Flash messages
// $("#close-message").on("click", closeFlash);

// function closeFlash(){
//     $("#flash-message").css("display", "none");
//     return false;
// }


// ----- CODE CREDIT -----
// https://stackoverflow.com/questions/20437938/jquery-disappear-div-with-delay-then-appear-disappear-on-hover

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

// ----- END OF CODE CREDIT -----


// Landing page - banner - Materialize parallax effect
$(document).ready(function(){
    $('.parallax').parallax();
  });


// Materialize select field
  $(document).ready(function(){
    $('select').formSelect();
  });