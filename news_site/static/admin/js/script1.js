document.addEventListener("DOMContentLoaded", function() {
    const titleInput = document.getElementById('idTitle');
    const subtitleInput = document.getElementById('idSubtitle');
    const mainTextInput = document.getElementById('idMainText');

    const previewTitle = document.getElementById('previewTitle');
    const previewSubtitle = document.getElementById('previewSubtitle');
    const previewMainText = document.getElementById('previewMainText');

    titleInput.addEventListener('input', function() {
        previewTitle.textContent = titleInput.value;
    });
    subtitleInput.addEventListener('input', function() {
        previewSubtitle.textContent = subtitleInput.value;
    });

    mainTextInput.addEventListener('input', function() {
        updatePreviewMainText();
    });

    mainTextInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); 
            insertParagraph();
        }
    });

    function updatePreviewMainText() {
        const paragraphs = mainTextInput.value.split('\n');
        previewMainText.innerHTML = paragraphs.map(paragraph => `<p class="mb-1">${paragraph}</p>`).join('');
    }

    function insertParagraph() {
        const cursorPosition = mainTextInput.selectionStart;
        const textBefore = mainTextInput.value.substring(0, cursorPosition);
        const textAfter = mainTextInput.value.substring(cursorPosition);
        mainTextInput.value = textBefore + '\n' + textAfter;
        mainTextInput.selectionStart = cursorPosition + 1;
        mainTextInput.selectionEnd = cursorPosition + 1;
        updatePreviewMainText();
    }
});
