$(document).ready(function () {

    $("#error-nombre").hide()

    $("#nombre-txt").blur(function () {


        //VALIDACIÓN NOMBRE
        if ($("#nombre-txt").val().length < 3) {
            $("#error-nombre").html("El nombre esta vacio")
            $("#error-nombre").fadeIn()
        }

    });

    $("#nombre-txt").focus(function () {
        $("#error-nombre").fadeOut()

    });

    //Validar correo
    $("#error-correo").hide()

    $("#correo-contacto").blur(function () {


        if ($("#correo-contacto").val().length < 8) {
            $("#error-correo").html("El e-mail esta vacio")
            $("#error-correo").fadeIn()
        }

    });

    //ASUNTOS// 

    $("#error-asuntos").hide()

    $("#asuntos-txt").blur(function () {


        //VALIDACIÓN ASUNTOS
        if ($("#asuntos-txt").val().length < 3) {
            $("#error-asuntos").html("Escriba sus dudas en Asuntos")
            $("#error-asuntos").fadeIn()
        }


    });

    //MENSAJES//

    $("#error-mensajes").hide()

    $("#mensajes-txt").blur(function () {


        //VALIDACIÓN MENSAJES
        if ($("#asuntos-txt").val().length < 3) {
            $("#error-mensajes").html("Escriba un mensaje")
            $("#error-mensajes").fadeIn()
        }


    });

});

function FormularioEnviado(){
    alert("Formulario Enviado")



};


    
function DatosBorrados(){
    alert("Datos Borrados")
    
};