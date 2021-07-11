function sendMail(contactForm) {
    emailjs.send("service_611qf0k", "cookable", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "cookable_request": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            flashEmail = document.getElementById("flash-messages-email");
            flashEmail.style.display = 'inline-block';
            flashEmail.innerHTML = "Message sent successfully";
        },
        function(error) {
            console.log("FAILED", error);
            flashEmail = document.getElementById("flash-messages-email");
            flashEmail.style.display = 'inline-block';
            flashEmail.innerHTML = "Message not sent!";
        }
    );
    setTimeout(function(){window.location.reload();},4000);
    return false;
}