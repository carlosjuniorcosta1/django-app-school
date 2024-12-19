    document.addEventListener("DOMContentLoaded", function () {
    const filterButton = document.getElementById("filterButton");
    const chapterSelector = document.getElementById("chapterSelector");
    const chapterFilterForm = document.getElementById("chapterFilterForm");

    filterButton.addEventListener("click", function () {
        const selectedChapterId = chapterSelector.value;

        if (selectedChapterId) {
            const newUrl = `${chapterFilterForm.action}?chapter_id=${selectedChapterId}`;
            window.location.href = newUrl;
        } else {
            alert("Por favor, selecione um capítulo.");
        }
    });
});

