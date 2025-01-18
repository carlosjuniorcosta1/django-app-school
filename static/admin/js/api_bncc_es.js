document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("filtrar").addEventListener('click', function() {
        var materia = document.getElementById('materias').value;
        var ano = document.getElementById('anos').value;
        
        var searchP = new URLSearchParams(window.location.search);
        searchP.set('materia', materia);
        searchP.set('ano', ano);
        window.location.search = searchP.toString();
    });
});

$(document).ready(function() {
    $('.copy-icon').click(function() {
        var textToCopy = "";

        if ($(this).siblings('.copiable-text-lang').length) {
            textToCopy = $(this).siblings('.copiable-text-lang').text();
        } else {
            var codSkill = $(this).siblings('.copiable-text').text();
            var skill = $(this).siblings('span').last().text();
            textToCopy = codSkill + skill;
        }

        navigator.clipboard.writeText(textToCopy).then(() => {
            $(this).closest('tr').find('.copied-msg').remove();

            var copiedMsg = $('<span class="copied-msg">Copiado!</span>');
            $(this).after(copiedMsg);

            setTimeout(() => {
                copiedMsg.fadeOut(function() {
                    $(this).remove();
                });
            }, 1000);
        }).catch((error) => {
            console.error('Falha ao copiar o texto: ', error);
        });
    });
});
