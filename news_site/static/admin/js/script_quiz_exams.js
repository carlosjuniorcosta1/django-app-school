

const urlParams = new URLSearchParams(window.location.search);



function renderQuestions(questions) {
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


document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.getElementById("searchForm");
    const questionsContainer = document.getElementById("questionsContainer");
    const paginationContainer = document.getElementById("paginationContainer");

    const initialFilterBy = urlParams.get("filter_by") || "word";
    const initialSearchTerm = urlParams.get("search_term") || "";
    document.getElementById("filter_by").value = initialFilterBy;
    document.getElementById("search_term").value = initialSearchTerm;

    searchForm.addEventListener("submit", function (e) {
        e.preventDefault();
        performSearch(1);
    });

    function performSearch(page) {
        const filterBy = document.getElementById("filter_by").value;
        const searchTerm = document.getElementById("search_term").value;

        console.log(inputNumberQuestion)

        const urlParams = new URLSearchParams();
        urlParams.set("filter_by", filterBy);
        urlParams.set("search_term", searchTerm);
        urlParams.set("page", page);
        
        let currentPageClicked = urlParams.get('page')

        const url = `${window.location.pathname}?${urlParams.toString()}`;
        history.pushState(null, "", url)


        fetch(url, {
            headers: { "X-Requested-With": "XMLHttpRequest" },
        })
            .then((response) => response.json())
            .then((data) => {
                renderQuestions(data.questions);
                console.log(`Testando - total de páginas: ${data.total_pages} - questões: ${data.total_questions} página atual: ${currentPageClicked}` );
                renderPagination(currentPageClicked, data.total_pages);
            let totalFilteredQuestionsContainer = document.getElementById('total-filtered-questions')  
            totalFilteredQuestionsContainer.innerHTML = `<span class=font-weight-bold>${data.total_questions}</span> <span>questões encontradas</span>`
            let totalFilteredQuestionsContainerMobile = document.getElementById('total-filtered-questions-mobile')  
            totalFilteredQuestionsContainerMobile.innerHTML = `<span class=font-weight-bold>${data.total_questions}</span> <span>questões</span>`


            })
            .catch((error) => {
                console.error("Erro na busca:", error);
            });       


    }

function renderPagination(currentPage, totalPages) {
        paginationContainer.innerHTML = ""; 
    
        if (totalPages <= 1) return; 
    
        const range = 5; // Número de páginas antes e depois da atual
        const startPage = Math.max(1, parseInt(currentPage) - range);  // Garantir que currentPage seja um número inteiro
        const endPage = Math.min(totalPages, parseInt(currentPage) + range);  // Garantir que currentPage seja um número inteiro
    
        // Botão "Primeiro"
        const firstButton = document.createElement("button");
        firstButton.classList.add("btn", "btn-sm", "mx-1");
        const firstIcon = document.createElement('i')
        firstIcon.classList.add('fas', 'fa-angle-double-left')
        firstButton.appendChild(firstIcon)
        firstButton.addEventListener("click", function () {
            performSearch(1);
        });
        paginationContainer.appendChild(firstButton);
    
        // Botão "Anterior"

        var buttonGreenLast = document.getElementById('buttonGreenLast')
        
        buttonGreenLast.addEventListener('click', function(){
            performSearch(parseInt(currentPage) - 1);
        })
        const prevButton = document.createElement("button");
        prevButton.classList.add("btn", "btn-sm");
        const prevIcon = document.createElement("i");
        prevIcon.classList.add("fas", "fa-arrow-left")
        prevButton.appendChild(prevIcon)
    
    
        if (parseInt(currentPage) > 1) {  // Garantir que currentPage seja um número inteiro
            prevButton.addEventListener("click", function () {
                performSearch(parseInt(currentPage) - 1);
            });
        } else {
            prevButton.disabled = true;
            firstButton.disabled = true // Desabilita o botão se não houver página anterior
        }
        paginationContainer.appendChild(prevButton);
    
        // Páginas anteriores à atual (máximo 5)
        for (let page = startPage; page < parseInt(currentPage); page++) {  // Garantir que currentPage seja um número inteiro
            const pageButton = document.createElement("button");
            pageButton.classList.add("btn", "btn-sm", "mx-1", "btn-secondary");
            pageButton.textContent = page;
            pageButton.addEventListener("click", function () {
                performSearch(page);
            });
            paginationContainer.appendChild(pageButton);
        }
    
        // Página atual
        const currentPageButton = document.createElement("button");
        currentPageButton.classList.add("btn", "btn-sm", "mx-1", "btn-primary");
        currentPageButton.textContent = currentPage;
        paginationContainer.appendChild(currentPageButton);
    
        // Páginas seguintes à atual (máximo 5)
        for (let page = parseInt(currentPage) + 1; page <= endPage; page++) {  // Garantir que currentPage seja um número inteiro
            const pageButton = document.createElement("button");
            pageButton.classList.add("btn", "btn-sm", "mx-1", "btn-secondary");
            pageButton.textContent = page;
            pageButton.addEventListener("click", function () {
                performSearch(page);
            });
            paginationContainer.appendChild(pageButton);
        }
    
        // Botão "Próximo"
        var buttonGreenNext = document.getElementById('buttonGreenNext')
        
        buttonGreenNext.addEventListener('click', function(){
            performSearch(parseInt(currentPage) + 1);
        })
        const nextButton = document.createElement("button");
        nextButton.classList.add("btn", "btn-sm");
        const nextIcon = document.createElement("i");
        nextIcon.classList.add("fas", "fa-arrow-right"); // Altere 'fa-arrow-right' pelo ícone desejado
        nextButton.appendChild(nextIcon);
    
        if (parseInt(currentPage) < totalPages) {  // Garantir que currentPage seja um número inteiro
            nextButton.addEventListener("click", function () {
                performSearch(parseInt(currentPage) + 1);

            });
        } else {
            nextButton.disabled = true; 
            lastButton.disabled = true// Desabilita o botão se não houver página seguinte
        }
        paginationContainer.appendChild(nextButton);
    
        // Botão "Último"

        const lastButton = document.createElement("button");
        lastButton.classList.add("btn", "btn-sm", "mx-1");
        const lastIcon = document.createElement('i')
        lastIcon.classList.add('fas', 'fa-angle-double-right')
        lastButton.appendChild(lastIcon)
        lastButton.addEventListener("click", function () {
            performSearch(totalPages);
        });
        
        paginationContainer.appendChild(lastButton);
 
        }     
    


document.getElementById('goToButton').addEventListener('click', function(e) {
    e.preventDefault()
    const inputNumberQuestion = document.getElementById('inputNumberQuestion').value;


    urlParams.set('page', inputNumberQuestion)
    const url = `${window.location.pathname}?${urlParams.toString()}`;
    history.pushState(null, "", url)

    fetch(url, {
        headers: { "X-Requested-With": "XMLHttpRequest" },
    })
        .then((response) => response.json())
        .then((data) => {      

      
            renderQuestions(data.questions);  // Exibindo as questões
            renderPagination(inputNumberQuestion, data.total_pages);



        })
        .catch((error) => {
            console.error("Erro na busca:", error);
        });    

}
)

    window.checkAnswer = function (questionId) {
        const selectedAnswer = document.querySelector(`input[name="answer-${questionId}"]:checked`);
        if (selectedAnswer) {
            const isCorrect = selectedAnswer.value === "true"; 
            const selectedLabel = selectedAnswer.closest('.form-check');

            const allFormChecks = document.querySelectorAll(`.form-check`);
            allFormChecks.forEach((formCheck) => {
                formCheck.classList.remove("bg-success", "bg-danger");
            });

            if (isCorrect) {
                selectedLabel.classList.add("bg-success");
            } else {
                selectedLabel.classList.add("bg-danger");
            }
        } else {
            alert("Por favor, selecione uma resposta antes de enviar!");
        }
    };
    const initialPage = urlParams.get("page") || 1;
    performSearch(initialPage);


})






