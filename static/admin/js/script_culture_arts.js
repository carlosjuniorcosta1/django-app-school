$(document).ready(function() {
    // Título a ser animado para a primeira seção (Ilustrações para usuários)
    var titleText = "Ilustrações para usuários"; // Título da primeira seção
    var titleContainer = $('#animated-title');

    // Animação das cartas da primeira seção
    $('.animation-card').each(function(index) {
        $(this).hide().delay(index * 400).fadeIn(2000); 
    });

    // Animação do título da primeira seção
    titleText.split('').forEach(function(letter, index) {
        setTimeout(function() {
            titleContainer.append(letter);
        }, index * 100); 
    });

    // Função para verificar se todas as cartas da primeira seção foram carregadas
    function checkFirstSectionLoaded() {
        var allLoaded = true;

        $('.animation-card').each(function() {
            if (!$(this).is(':visible')) {
                allLoaded = false;
                return false; // Sai do loop
            }
        });

        return allLoaded;
    }

    // Função que anima o título da segunda seção após a primeira estar carregada
    function loadSecondSection() {
        var titleText2 = "Tirinhas"; // Título da segunda seção
        var titleContainer2 = $('#animated-title-2');

        // Verifica se todas as cartas da primeira seção foram carregadas
        if (checkFirstSectionLoaded()) {
            titleText2.split('').forEach(function(letter, index) {
                setTimeout(function() {
                    titleContainer2.append(letter);
                }, index * 200); 
            });

            $('.animation-card-2').each(function(index) {
                $(this).hide().delay(index * 400).fadeIn(3000);
            });
        }
    }

    // Intervalo para verificar continuamente o carregamento da primeira seção
    var checkInterval = setInterval(function() {
        if (checkFirstSectionLoaded()) {
            clearInterval(checkInterval); // Para de verificar quando a primeira seção está carregada
            loadSecondSection(); // Carrega a segunda seção
        }
    }, 500);

    // Animação de flip nas cartas (card-flip)
    document.querySelectorAll('.card-flip').forEach(card => {
        card.addEventListener('click', function() {
            // Alterna a classe 'flip' ao clicar na carta
            this.classList.toggle('flip');
        });
    });
});
