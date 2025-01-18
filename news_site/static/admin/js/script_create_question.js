document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll('input[name$="-alternative"]').forEach(function (input) {
            const container = input.closest('p, div'); 
            if (container) {
                container.style.display = "none"; 
            }
        });
  


    });
    document.getElementById('add-answer').addEventListener('click', function() {

        const formsetDiv = document.getElementById('answer-formset');
        const totalForms = document.getElementById('id_answer_set-TOTAL_FORMS');
        const currentIndex = parseInt(totalForms.value, 10);

        const newForm = formsetDiv.querySelector('.answer-item:last-child').cloneNode(true);
        formsetDiv.appendChild(newForm);

        newForm.querySelectorAll('input, select, textarea').forEach(function(input) {
            input.name = input.name.replace(`-${currentIndex - 1}-`, `-${currentIndex}-`);
            input.id = input.id.replace(`-${currentIndex - 1}-`, `-${currentIndex}-`);
            input.value = '';  
        });

        totalForms.value = currentIndex + 1;
    });

    document.getElementById('answer-formset').addEventListener('click', function(e) {
        if (e.target.classList.contains('remove-answer')) {
            const answerItem = e.target.closest('.answer-item');
            if (document.querySelectorAll('.answer-item').length > 1) {
                answerItem.remove();
                const totalForms = document.getElementById('id_answer_set-TOTAL_FORMS');
                totalForms.value = parseInt(totalForms.value, 10) - 1;
            } else {
                alert('Deve haver pelo menos uma alternativa.');
            }
        }

    });