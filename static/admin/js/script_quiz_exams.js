document.addEventListener("DOMContentLoaded", function () {
    


    const searchForm = document.getElementById("searchForm");

    const questionsContainer = document.getElementById("questionsContainer");
    const paginationContainer = document.getElementById("paginationContainer");

    const urlParams = new URLSearchParams(window.location.search);
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

        const urlParams = new URLSearchParams();
        urlParams.append("filter_by", filterBy);
        urlParams.append("search_term", searchTerm);
        urlParams.append("page", page);

        const url = `${window.location.pathname}?${urlParams.toString()}`;

        fetch(url, {
            headers: { "X-Requested-With": "XMLHttpRequest" },
        })
            .then(response => response.json())
            .then(data => {
                renderQuestions(data.questions);
                renderPagination(data.current_page, data.total_pages);
            })
            .catch(error => {
                console.error("Erro na busca:", error);
            });
    }

    function renderQuestions(questions) {
        questionsContainer.innerHTML = ""; 
        if (questions.length === 0) {
            questionsContainer.innerHTML = "<p class='text-center'>Nenhuma questão encontrada.</p>";
        } else {
            questions.forEach(question => {
                const questionDiv = document.createElement("div");
                questionDiv.classList.add("card", "mb-3");
                questionDiv.innerHTML = `<div class="card-body"><p class=text-question>(${question.examining_board}) - ${question.context}</p> `

                         if(question.question){
                            questionDiv.innerHTML += `                            
                        <p class="font-weight-bold text-question ml-3">${question.question}</p> `
                        questionDiv.innerHTML += `
                        <div class="question-images">
                            ${question.images ? question.images.map(image => `
                                <img src="${image}" alt="Imagem da Pergunta" class="question-image img-fluid mb-3" />
                            `).join("") : ""}
                        </div>
                        <ul id="answers-${question.id}" class="list-group"></ul>
                        <div class="d-flex justify-content-between align-items-start mt-1">
    <button type="button" class="btn btn-primary btn-sm" onclick="checkAnswer(${question.id})">Responder</button>
    <div class="mr-auto d-flex">
        <a class="btn btn-success btn-sm mx-1" id="buttonScrollDown">
            <i class="fa-solid fa-arrow-down"></i>
        </a>
        <a class="btn btn-success btn-sm" id="buttonScrollUp">
            <i class="fa-solid fa-arrow-up"></i>
        </a>
    </div>
</div>

                        <p style="display:none" id="showAlertQuestion"> </p>
                    </div>                                    
                            `
                            }

                questionsContainer.appendChild(questionDiv);

                const answersContainer = document.getElementById(`answers-${question.id}`);
                question.answers.forEach((answer, index) => {
                    const option = document.createElement("div");
                    option.classList.add("form-check", "mb-2", "d-flex", "align-items-center", "ml-1");
                    const answerText = answer.text && answer.text.trim() !== "" ? answer.text : null;

                    option.innerHTML = `
                    <input type="radio" name="answer-${question.id}" id="answer-${question.id}-${index}" value="${answer.is_correct}" class="form-check-input">
                    <label for="answer-${question.id}-${index}" class="form-check-label d-flex align-items-center">
                        ${answerText ? `${answer.alternative}) <span class="border-bottom mb-1 mt-2 text-answer" style="margin-left: 0.5em;">${answerText}</span>` : 
                        (answer.images && answer.images.length > 0 ? answer.images.map(image => `
                           <span> ${answer.alternative}) </span> <img src="${image}" alt="Imagem da Resposta" class="answer-image img-fluid border-bottom mb-1 mt-2" />
                        `).join("") : "Texto não disponível")}
                    </label>
                `;
                
                    answersContainer.appendChild(option);
                });
            });
        }
    }

    function renderPagination(currentPage, totalPages) {
        paginationContainer.innerHTML = ""; 

        if (totalPages > 1) {
            if (currentPage > 1) {
                const prevButton = document.createElement("button");
                prevButton.classList.add("btn", "btn-secondary", "mr-2");
                prevButton.textContent = "Anterior";
                prevButton.onclick = () => performSearch(currentPage - 1);
                paginationContainer.appendChild(prevButton);
            }

            if (currentPage < totalPages) {
                const nextButton = document.createElement("button");
                nextButton.classList.add("btn", "btn-secondary");
                nextButton.textContent = "Próxima";
                nextButton.onclick = () => performSearch(currentPage + 1);
                paginationContainer.appendChild(nextButton);
            }
        }
    }

    window.checkAnswer = function(questionId) {
        const selectedAnswer = document.querySelector(`input[name="answer-${questionId}"]:checked`);
        if (selectedAnswer) {
            const isCorrect = selectedAnswer.value === "true"; 
            const selectedLabel = selectedAnswer.closest('.form-check')

            const allformChecks = document.querySelectorAll(`.form-check`);
            allformChecks.forEach(formcheck=> {
                formcheck.classList.remove("bg-success", "bg-danger");
            });

            if (isCorrect) {
                selectedLabel.classList.add("bg-success"); 
            } else {
                selectedLabel.classList.add("bg-danger"); 
            }
        } else {
            alert("Por favor, selecione uma resposta antes de enviar!");
        }
    }

    const initialPage = urlParams.get("page") || 1;
    performSearch(initialPage);
});


document.addEventListener('click', function(e){
    const cards = document.querySelectorAll(".text-question.card");

    if(e.target.closest("#buttonScrollDown")){
        console.log('cliquei')
    }

}
)

document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("click", function (e) {
        if (e.target.closest("#buttonScrollDown")) {
            const currentCard = e.target.closest(".card");

            if (currentCard) {
                const nextCard = currentCard.nextElementSibling;

                if (nextCard) {
                    const nextCardBody = nextCard.querySelector(".card-body");

                    if (nextCardBody) {
                        nextCardBody.scrollIntoView({
                            behavior: "smooth",
                            block: "start"
                        });
                    } 
                } else {
                    alert("Não há mais questões!");
                }
            }
        }
    });
});



document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("click", function (e) {
        if (e.target.closest("#buttonScrollUp")) {
            const currentCard = e.target.closest(".card");

            if (currentCard) {
                const lastCard = currentCard.previousElementSibling;

                if (lastCard) {
                    const lastCardBody = lastCard.querySelector(".card-body");

                    if (lastCardBody) {
                        lastCardBody.scrollIntoView({
                            behavior: "smooth",
                            block: "start"
                        });
                    }
                } else {
                    alert("Não há mais questões!");
                }
            }
        }
    });
});
