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
