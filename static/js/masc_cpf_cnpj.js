
jQuery(document).ready(function($) {
    //$("input[name=rg]").mask('999.999-9');
    //$("input[name=orgao]").mask('aaa/aa');

    //Mascara para telefone residencial e celular
    $('input[id*="telefone_res"]').mask("(99) 9999-9999");

    $('input[id*="telefone_cel"]').mask("(99) 9999-9999?9");
    $('input[id*="telefone_cel"]').keyup(function () {
        var cel;

        cel = $(this).val().replace(/\D/g, '');

        if (cel.length > 10) {
            $(this).unmask();
            $(this).mask("(99) 99999-9999");

        } else if (cel.length == 10) {
            $(this).unmask();
            $(this).mask("(99) 9999-9999?9");
        }

    }).trigger('keyup');


    //Mascara para CPF e CNPJ
    $("input[id*=cpf_cnpj]").mask("999.999.999-99?999");
    $('input[id*=cpf_cnpj]').on('keyup', function (e) {

        var cpf = $(this).val().replace(/[^0-9]+/g, '');

        if (cpf.length == 11) {
            $(this).mask("999.999.999-99?999");
        }

        if (cpf.length == 14) {
            $(this).mask("99.999.999/9999-99");
        }
    });


});
//letras e numeros
//var query = $(this).val().replace(/[^a-zA-Z 0-9]+/g, '');