$(document).ready(function () {

    $("#error-titulo").hide()

    $("#titulo-agre").blur(function () {


        //VALIDACIÓN Titulo
        if ($("#titulo-agre").val().length < 3) {
            $("#error-titulo").html("El titulo de la obra esta vacio")
            $("#error-titulo").fadeIn()
        }

    });

    $("#error-comentarios").hide()

    $("#coment-agre").blur(function () {


        //VALIDACIÓN DESCRIPCION
        if ($("#coment-agre").val().length < 3) {
            $("#error-comentarios").html("Comente la obra")
            $("#error-comentarios").fadeIn()
        }

    });

});


function ObraAgregada(){
    alert("Obra Agregada")



};


    
function ObraEliminada(){
    alert("Obra Eliminada")
    
};
