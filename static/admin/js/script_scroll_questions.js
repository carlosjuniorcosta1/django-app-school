
document.addEventListener('click', function(e){
    const cards = document.querySelectorAll(".text-question.card");

    if(e.target.closest("#buttonScrollDown")){
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

