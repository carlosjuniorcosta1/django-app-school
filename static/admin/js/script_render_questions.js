export function renderQuestions(questions) {
    questionsContainer.innerHTML = ""; 
    if (questions.length === 0) {
        questionsContainer.innerHTML = "<p class='text-center'>Nenhuma questão encontrada.</p>";
    } else {
        questions.forEach((question) => {  
     
            const questionDiv = document.createElement("div");
            questionDiv.classList.add("card", "mb-3");

            let questionImageHTML = "";
            if (question.question_image) {
                questionImageHTML = `
                    <div class="mb-3">
                        <img src="${question.question_image}" alt="Imagem da pergunta" class="img-fluid">
                    </div>
                `;
            }
         if(question.question && question.context){
            questionDiv.innerHTML = `<div class="card-body"><p class=text-question><span class=numberQuestion>${question.number}</span> -
             (${question.examining_board ? question.examining_board.toUpperCase() : "Banca não cadastrada"}) - ${question.context}}</p>`;
        }
        else if(question.question && !question.context){
            questionDiv.innerHTML = `<div class="card-body"><p class=text-question><span class=numberQuestion>${question.number}</span> - 
            (${question.examining_board ? question.examining_board.toUpperCase() : "Banca não cadastrada"}) - ${question.question}</p>`;

        }        
            if (question.question) {
                questionDiv.innerHTML += `
                    <div class="img-question">
                        ${questionImageHTML}
                    </div>
                    <ul id="answers-${question.id}" class="list-group"></ul>
                    <div class="d-flex justify-content-between align-items-start mt-1">
                        <button type="button" class="btn btn-primary btn-sm" onclick="checkAnswer(${question.id})">Responder</button>
                        <div class="mr-auto d-flex">
                            <a class="btn btn-success btn-sm mx-1" id="buttonGreenLast">
                                <i class="fa-solid fa-arrow-left"></i>
                            </a>
                            <a class="btn btn-success btn-sm" id="buttonGreenNext">
                                <i class="fa-solid fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                    <p style="display:none" id="showAlertQuestion"> </p>
                </div>`;
            }

            questionsContainer.appendChild(questionDiv);

           const answersContainer = document.getElementById(`answers-${question.id}`);
            question.answers.forEach((answer, index) => {
                const option = document.createElement("div");
                option.classList.add("form-check", "mb-2", "ml-1");

                let answerContent = "";
                if (answer.answer_image) {
                    answerContent = `<div>
                   ${answer.total_answers > 2 ? `<span> ${answer.alternative})</span>`: ""}
                        <img src="${answer.answer_image}" alt="Imagem da Resposta" class="img-answer border-bottom mb-1 mt-2 ml-2" />
                    </div>`;
                } else if (answer.text && answer.text.trim() !== "") {
                    answerContent = `
                        <div>
                            ${answer.total_answers > 2 ? `<span>${answer.alternative})</span>` : ""}
                            <span class="text-answer">${answer.text}</span>
                        </div>`;
                } else {
                    answerContent = "Texto não disponível";
                }

                option.innerHTML = `
                    <input type="radio" name="answer-${question.id}" id="answer-${question.id}-${index}" value="${answer.is_correct}" class="form-check-input">
                    <label for="answer-${question.id}-${index}" class="form-check-label d-flex align-items-center">
                        ${answerContent}
                    </label>
                `;

                answersContainer.appendChild(option);
            });
        });
    }
}