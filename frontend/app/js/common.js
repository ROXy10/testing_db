$(function () {
    //MODAL FORM
    modalForm(document.getElementById('modalForm'),
        document.getElementById("singInNav"),
        document.getElementsByClassName("modal-form__close")[0]
    );
    modalForm(document.getElementById('modalForm'),
        document.getElementById("singIn"),
        document.getElementsByClassName("modal-form__close")[0]
    );
    // MODAL FROM END

    // FOOTER COPYRIGHT
    $('#copyright').text('© ' + new Date().getFullYear() + ' Тестування.');
    // FOOTER COPYRIGHT END
});

function modalForm(modal, btn, span) {
    // When the user clicks the button, open the modal
    btn.onclick = function () {
        modal.style.display = "block";
    };

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}