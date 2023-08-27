
/* Menu Toggle List */
$(document).ready(function () {
    $(".menu-icon").click(function () {
        $(".right-wrapper").toggleClass('hide');
    });
});

/* Drop Down Menu */
$(document).ready(function() {
    $('select').niceSelect();  
    $('select:not(.ignore)').niceSelect();    
});   

/* Popup Window */
$(document).ready(function () {
    const modal = document.querySelector("#subscribe-modal");
    const openModal = document.querySelector("#subscribe-btn");
    const closeModal = document.querySelector("#subscribe-close");
    openModal.addEventListener('click', function(){
        modal.showModal();
    })
    closeModal.addEventListener('click', function(){
        modal.close();
    })
});

/* Prevent Form Resubmission */
if (window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}

/* Close Flash Messages */
$(document).ready(function () {
    $(".flash-close").click(function () {
        $(".flash-message").fadeOut(250);
    });
});
$(document).ready(function () {
    setTimeout(function() {
        $('.flash-message').fadeOut(250);
    }, 10000);
});

/* Accordian Section */
$(document).ready(function () {
    $("#accordion-support-wrapper").click(function () {
        $("#accordion-support-content").slideToggle();
    });
    $("#accordion-contributors-wrapper").click(function () {
        $("#accordion-contributors-content").slideToggle();
    });
    $("#accordion-terms-wrapper").click(function () {
        $("#accordion-terms-content").slideToggle();
    });
});