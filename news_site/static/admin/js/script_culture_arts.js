
$(document).ready(function() {
    // Título a ser animado
    var titleText = "Ilustrações para usuários"; // Altere para o seu título
    var titleContainer = $('#animated-title');
    var title2Container = $('#animated-title-2')
    $('.animation-card').each(function(index) {
        $(this).hide().delay(index * 400).fadeIn(2000); 
    });
    titleText.split('').forEach(function(letter, index) {
        setTimeout(function() {
            titleContainer.append(letter);
        }, index * 100); 
    });
});


$(document).ready(function() {
    // Título a ser animado
    var titleText2 = "Tirinhas"; // Altere para o seu título
    var titleContainer2 = $('#animated-title-2')
    $('.animation-card-2').each(function(index) {
        $(this).hide().delay(index * 400).fadeIn(3000);
    });
    titleText2.split('').forEach(function(letter, index) {
        setTimeout(function() {
            titleContainer2.append(letter);
        }, index * 300); 
    });
});










document.querySelectorAll('.card-flip').forEach(card => {
    card.addEventListener('click', function() {
        // Alterna a classe 'flip' no card clicado
        this.classList.toggle('flip');
    });
});
