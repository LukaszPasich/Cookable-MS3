// Materialize initialization

$(document).ready(function () {

    // Materialize mobile navbar
    $('.sidenav').sidenav({edge: "right"});

    // Materialize parallax effect
    $('.parallax').parallax();

    // Materialize select field
    $('select').formSelect();

    // Materialize delete recipe modal
    $('.modal').modal();


    // ----- CODE CREDIT -----
    // Code Institute Tutorial (Backend Development | Mini Project | Adding a task - Writing to the Database | Materialize Form Validation)

    // Validate Materialize select
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
    // ----- END OF CODE CREDIT -----
});


// ----- CODE CREDIT - Animated flash message -----
// https://stackoverflow.com/questions/20437938/jquery-disappear-div-with-delay-then-appear-disappear-on-hover

$(document).ready( function() {
    setTimeout(function () {
        $("#flash-message")
            .animate({
                'opacity': 0
            }, 750);
    },5000);
});

// ----- END OF CODE CREDIT -----


// ----- CODE CREDIT - Confirm password matching validation -----
// https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518

$('#password, #confirm_password').on('keyup', function () {
    // I've added check for password length so that empty passwords at the beginining don't result in match
    if ($('#password').val() == $('#confirm_password').val() && $('#password').val().length > 0) {
      $('#password-match-message').html("Passwords match").css('color', 'green');
      $('#signup-button').css('display', 'block');
      $('#signup-button-inactive').css('display', 'none');
    } else {
      $('#password-match-message').html("Passwords don't match").css('color', 'red');
      $('#signup-button').css('display', 'none');
      $('#signup-button-inactive').css('display', 'block');
}});

// ----- END OF CODE CREDIT -----
