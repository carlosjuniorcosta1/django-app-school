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
    let isPremium = preVerificationDiv.getAttribute('data-is-premium') 
    let buttonSubmit = document.getElementById('buttonSubmit')
    let paginationButtons = document.getElementById('pagination-buttons')

    let noPremium = document.getElementById('no-premium')

    console.log("Valor de isPremium:", isPremium);
    

    if (isPremium !== 'true') {
        noPremium.style.display = 'block';
        buttonSubmit.style.display = 'none'; 
        paginationButtons.style.display = 'none' 

        return; // 
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const quizForm = document.getElementById("quiz-form");

    if (!quizForm) return;

    // Verifica se o filtro foi usado com base no atributo data-is-filter-used
    const isFilterUsed = quizForm.getAttribute("data-is-filter-used") === "true";

    if (isFilterUsed) {
        quizForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Impede o comportamento padrão de envio do formulário

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
                    // Substitui o conteúdo do formulário
                    const container = document.querySelector(".container");
                    container.innerHTML = html;

                    // Rola até a pergunta
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
