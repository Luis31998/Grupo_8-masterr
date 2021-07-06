$(document).ready(function () {

    $("#error-nom1").hide()

    $("#nombre").blur(function () {


        //VALIDACIÓN NOMBRE
        if ($("#nombre").val().length < 3) {
            $("#error-nom1").html("El Nombre esta vacio")
            $("#error-nom1").fadeIn()
        }

    });

    $("#nombre").focus(function () {
        $("#error-nom1").fadeOut()

    });


    //VALIDACIÓN APELLIDOS// 

    $("#error-ap1").hide()

    $("#apellido").blur(function () {


        //VALIDACIÓN
        if ($("#apellido").val().length < 5) {
            $("#error-ap1").html("El Apellido esta vacio")
            $("#error-ap1").fadeIn()
        }

    });

    $("#apellido").focus(function () {
        $("#error-ap1").fadeOut()

    });


    //VALIDACIÓN EMAIL//

    $("#error-email").hide()

    $("#email-reg").blur(function () {

        //VALIDACIÓN//
        if ($("#email-reg").val().length < 8) {
            $("#error-email").html("El e-mail esta vacio")
            $("#error-email").fadeIn()
        }

    });

    $("#email-reg").focus(function () {
        $("#error-email").fadeOut()

    });

    //VALIDACIÓN CONTRASEÑA

    $("#form-reg").submit(function () {
        console.log("Submit")

        var pass = $("#cont-reg").val()

        if (pass.length < 8) {
            $("#cont-error").html("Contraseña debe tener 8 caracteres")
            event.preventDefault()
        }

    });

    //

    $.getJSON(
        'https://apis.digital.gob.cl/dpa/regiones/05/comunas', //URL API
        function (data) {  //QUE HACER CON LOS DATOS
            //Cargar comunas al combobox
            $.each(data, function (i, item) {
                $("#comunas").append(
                    '<option value="' + item.codigo + '">' + item.nombre + '</option>'
                );
            })
        }
    );


});

function RegistroEnviado(){
    alert("Registro Enviado")



};


    
function DatosBorrados(){
    alert("Datos Borrados")
    
};
