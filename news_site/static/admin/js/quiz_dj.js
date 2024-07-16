document.addEventListener('DOMContentLoaded', function() {
    let button = document.getElementById('buttonSubmit');
    let questions = document.querySelectorAll('.quiz-question');
        button.addEventListener('click', function(event) {    
            event.preventDefault()
            questions.forEach(function(question) {
                let selectedAnswer = question.querySelector("input[type='radio']:checked")
                if(selectedAnswer){
                    
                    let isCorrectAnswer = selectedAnswer.dataset.isCorrect === 'true'
                    let wrongAnswer = selectedAnswer.dataset.isCorrect === 'false'
                    if(isCorrectAnswer) {


                        let labelElement = selectedAnswer.nextElementSibling;
                        labelElement.classList.remove('correct-answer-color')
                        labelElement.classList.add('correct-answer-color')

                    } 
                    if(wrongAnswer) {
                        let labelElement = selectedAnswer.nextElementSibling;
                        labelElement.classList.add('wrong-answer-color')

                    }
                }

                
            })

            })                
        });

document.getElementById('clearButton').addEventListener('click', function(){
    element.preventDefault()

    document.querySelectorAll('.correct-answer-color', 'wrong-answer-color').forEach(function(element){
        element.classList.remove('.correct-answer-color', 'wrong-answer-color')
    })
})
