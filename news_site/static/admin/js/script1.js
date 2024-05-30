document.addEventListener("DOMContentLoaded", function() {
    const titleInput = document.getElementById('id_title');
    const subtitleInput = document.getElementById('id_subtitle');
    const mainTextInput = document.getElementById('id_main_text');
    const imageInput = document.getElementById('id_image');
    const previewImage = document.getElementById('preview-image');
    const imageFilename = document.getElementById('image-filename');

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

    imageInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewImage.style.display = 'block';
            };
            reader.readAsDataURL(file);
            imageFilename.textContent = file.name; 
        } else {
            previewImage.src = '#';
            previewImage.style.display = 'none';
            imageFilename.textContent = ''; 
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
        mainTextInput.value = textBefore + '\n\n' + textAfter;
        mainTextInput.selectionStart = cursorPosition + 2;
        mainTextInput.selectionEnd = cursorPosition + 2;
        updatePreviewMainText();
    }

    updatePreviewMainText();
});
