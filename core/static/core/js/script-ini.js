$(document).ready(function () {
    //Validar correo
    $("#error-email-ini").hide()

    $("#email-ini").blur(function () {


        if ($("#email-ini").val().length < 8) {
            $("#error-email-ini").html("El e-mail esta vacio")
            $("#error-email-ini").fadeIn()
        }

    });

    $("#email-ini").focus(function () {
        $("#error-email-ini").fadeOut()

    });

    //Validar contraseña
    $("#form-ini").submit(function () {
        console.log("Submit")

        var pass = $("#cont-ini").val()

        if (pass.length < 8) {
            $("#cont-error-ini").html("Contraseña debe tener 8 caracteres")
            event.preventDefault()
        }

    });

});

function SesionIniciada(){
    alert("La sesion ha sido iniciada Correctamente")

};
