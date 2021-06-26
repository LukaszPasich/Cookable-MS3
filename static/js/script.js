// Mobile navbar
$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"});
});

// Close Flash messages
$("#close-message").on("click", closeFlash);

function closeFlash(){
    $("#flash-message").css("display", "none");
    return false;
}