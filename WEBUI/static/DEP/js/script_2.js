"use strict";

$(document).ready(function() {
    $(".modular_btn").click(function(event){

        $.ajax({
            type: "POST",
            url: "/modular",
            async: true,
            data: {
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                'method': $(this).attr("id")
            },
            success: function(response) {
//                $("#modal_other").css( "maxWidth", ( $( window ).width() * 0.9 | 0 ) + "px" );
//                $('#modal_other').find('.modal_other_text').text(response['output']);
//                $("#modal_other").modal({
//                    closeExisting: false
//                });
            },
            error: function(response) {
//                $("#modal_other").css( "maxWidth", ( $( window ).width() * 0.9 | 0 ) + "px" );
//                $('#modal_other').find('.modal_other_text').text(response['output']);
//                $("#modal_other").modal({
//                    closeExisting: false
//                });
            }
        });
    });

      
    
$(".generate_csr").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/renewmdm",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'gen_csr': 'ven_csr'
       }
   });
});

$(".download_csr").click(function(e){
    event.preventDefault();
   $.ajax({
       type: "POST",
       url: "/renewmdm",
       async: true,
       data: {
           'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
           'dwn_csr': 'get_csr'
       }
   });
});


});

