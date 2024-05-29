document.addEventListener("DOMContentLoaded", function() {
    const titleInput = document.getElementById('id_title');
    const subtitleInput = document.getElementById('id_subtitle');
    const mainTextInput = document.getElementById('id_main_text');

    const previewTitle = document.getElementById('preview-title');
    const previewSubtitle = document.getElementById('preview-subtitle');
    const previewMainText = document.getElementById('preview-text');

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
        previewMainText.innerHTML = mainTextInput.value;
    }

    function insertParagraph() {
        const cursorPosition = mainTextInput.selectionStart;
        const textBefore = mainTextInput.value.substring(0, cursorPosition);
        const textAfter = mainTextInput.value.substring(cursorPosition);
        const newText = textBefore + '<p class="mb-1"></p>' + textAfter;
        mainTextInput.value = newText;
        mainTextInput.selectionStart = cursorPosition + 16; // Move cursor inside the new <p> tag
        mainTextInput.selectionEnd = cursorPosition + 16;
        updatePreviewMainText();
    }

    updatePreviewMainText();
});
