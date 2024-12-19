document.addEventListener('DOMContentLoaded', function() {
    let button = document.getElementById('buttonSubmit');
    let questions = document.querySelectorAll('.quiz-question');

    button.addEventListener('click', function(event) {    
        event.preventDefault();
        
        questions.forEach(function(question) {
            let selectedAnswer = question.querySelector("input[type='radio']:checked");
            if (selectedAnswer) {
                let isCorrectAnswer = selectedAnswer.dataset.isCorrect === 'true';
                let wrongAnswer = selectedAnswer.dataset.isCorrect === 'false';
                let labelElement = selectedAnswer.parentElement;

                if (isCorrectAnswer) {
                    labelElement.classList.remove('wrong-answer-color');
                    labelElement.classList.add('correct-answer-color');
                } 
                if (wrongAnswer) {
                    labelElement.classList.remove('correct-answer-color');
                    labelElement.classList.add('wrong-answer-color');
                }
            }
        });

        setTimeout(function() {
            questions.forEach(function(question) {
                let selectedAnswer = question.querySelector("input[type='radio']:checked");
                if (selectedAnswer) {
                    let labelElement = selectedAnswer.parentElement;
                    labelElement.classList.remove('correct-answer-color', 'wrong-answer-color');
                }
            });
        }, 5000);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    let preVerificationDiv = document.getElementById('preVerification');
    let isPremium = preVerificationDiv ? preVerificationDiv.getAttribute('data-is-premium') : 'false';

    let buttonSubmit = document.getElementById('buttonSubmit');
    let paginationButtons = document.getElementById('pagination-buttons');
    let noPremium = document.getElementById('no-premium');

    console.log("Valor de isPremium:", isPremium); 

    if (isPremium !== 'true') {
        if (noPremium) noPremium.style.display = 'block'; 
        if (buttonSubmit) buttonSubmit.style.display = 'none'; 
        if (paginationButtons) paginationButtons.style.display = 'none'; 
        if (preVerificationDiv) preVerificationDiv.style.display = 'none'; 
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const quizForm = document.getElementById("quiz-form");

    if (!quizForm) return;

    const isFilterUsed = quizForm.getAttribute("data-is-filter-used") === "true";

    if (isFilterUsed) {
        quizForm.addEventListener("submit", function (event) {
            event.preventDefault(); // 

            const formData = new FormData(quizForm);
            const actionUrl = quizForm.getAttribute("action");

            fetch(actionUrl, {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                },
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error("Erro ao processar a solicitação.");
                    }
                    return response.text();
                })
                .then((html) => {
                    const container = document.querySelector(".container");
                    container.innerHTML = html;

                    const firstQuestion = document.querySelector(".text-question");
                    if (firstQuestion) {
                        firstQuestion.scrollIntoView({
                            behavior: "smooth",
                            block: "start",
                        });
                    }
                })
                .catch((error) => console.error("Erro ao enviar o formulário:", error));
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".text-question.card");
    if (cards.length > 0) {
        const lastCard = cards[cards.length - 1];

        const topOffset = lastCard.getBoundingClientRect().top + window.scrollY; 
        window.scrollTo({
            top: topOffset, 
            behavior: "smooth", 
        });
    }
});