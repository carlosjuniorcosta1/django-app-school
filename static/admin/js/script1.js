document.addEventListener("DOMContentLoaded", function () {
    const titleInput = document.getElementById('id_title');
    const subtitleInput = document.getElementById('id_subtitle');
    const mainTextInput = document.getElementById('id_main_text');
    const imageInput = document.getElementById('id_image');
    const previewImage = document.getElementById('preview-image');
    const imageFilename = document.getElementById('image-filename');
    const previewTitle = document.getElementById('preview-title');
    const previewSubtitle = document.getElementById('preview-subtitle');
    const previewMainText = document.getElementById('preview-text');
    const previewContainer = document.getElementById('preview-container');
    const ingredientsContainer = document.getElementById('ingredients-container');
    const preparationContainer = document.getElementById('preparation-container');
    const ingredientsPreview = document.getElementById('ingredients-preview');
    const preparationPreview = document.getElementById('preparation-preview');
    const genreSelect = document.getElementById('id_textual_genre');
    const sectionSelect = document.getElementById('id_section_name');
    const idArtist = document.getElementById('idArtist');
    const artistAtt = idArtist.getAttribute('data-is-artist');
    const selectedGenre = document.getElementById('selected-genre');
    const hideFields = document.getElementsByClassName('hide-ilustrator');
    const mainTextField = document.getElementById('box-main-text');
    const subtitleSelect = document.getElementById('box-subtitle');
    const askForIllustration = document.getElementById('ask-for-illustration');

    const allGenres = Array.from(genreSelect.options);
    const allowedGenresForIllustrations = ['tirinha', 'ilustração'];

    function capitalizeFirstLetter(text) {
        if (text.length === 0) return text;
        return text.charAt(0).toUpperCase() + text.slice(1);
    }

    function updatePreviewMainText() {
        const paragraphs = mainTextInput.value.split('\n');
        previewMainText.innerHTML = paragraphs.map(paragraph => `<p class="mb-1">${paragraph}</p>`).join('');
    }

    function showPreview() {
        previewSubtitle.style.display = 'block';
        previewMainText.style.display = 'block';
    }

    function hidePreview() {
        previewSubtitle.style.display = 'none';
        previewMainText.style.display = 'none';
    }

    function selectGenreByName(genre) {
        const genreOption = allGenres.find(option => option.text.toLowerCase() === genre.toLowerCase());
        if (genreOption) {
            genreSelect.value = genreOption.value;
        }
    }

    function selectSectionByName(section) {
        const sectionOption = Array.from(sectionSelect.options).find(option => option.text.toLowerCase() === section.toLowerCase());
        if (sectionOption) {
            sectionSelect.value = sectionOption.value;
        }
    }

    function syncFields() {
        const selectedGenre = genreSelect.options[genreSelect.selectedIndex].text.toLowerCase();
        const selectedSection = sectionSelect.options[sectionSelect.selectedIndex].text.toLowerCase();

        if (selectedSection === 'opinião') {
            if (['artigo', 'crônica'].includes(selectedGenre)) {
                showPreview();
            } else {
                selectGenreByName('artigo');
                showPreview();
            }
        } else if (selectedGenre === 'artigo') {
            selectSectionByName('opinião');
            showPreview();
        } else if (['conto', 'fanfic'].includes(selectedGenre)) {
            selectSectionByName('literatura');
            showPreview();
        } else if (['tirinha', 'ilustração'].includes(selectedGenre)) {
            selectSectionByName('ilustrações');
            showPreview();
        } else if (selectedGenre === 'receita') {
            selectSectionByName('comida');
            insertRecipeTemplate();
            hidePreview();
        }
    }

    titleInput.addEventListener('input', function () {
        const capitalizedTitle = capitalizeFirstLetter(titleInput.value);
        previewTitle.textContent = capitalizedTitle;
        titleInput.value = capitalizedTitle;
    });

    subtitleInput.addEventListener('input', function () {
        const capitalizedSubtitle = capitalizeFirstLetter(subtitleInput.value);
        previewSubtitle.textContent = capitalizedSubtitle;
        subtitleInput.value = capitalizedSubtitle;
    });

    mainTextInput.addEventListener('input', function () {
        updatePreviewMainText();
        updateRecipePreview();
    });

    imageInput.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
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

    genreSelect.addEventListener('change', function () {
        syncFields();
        toggleHideTextField();
    });

    sectionSelect.addEventListener('change', function () {
        const selectedSection = sectionSelect.options[sectionSelect.selectedIndex].text.toLowerCase();
        if (selectedSection === 'opinião') {
            addChronicleOption();
        } else {
            removeChronicleOption();
        }
        syncFields();
        toggleHideTextField();
    });

    function toggleIllustrationMenu() {
        const selectedGenreValue = genreSelect.options[genreSelect.selectedIndex].text.toLowerCase();
        const selectedSectionValue = sectionSelect.options[sectionSelect.selectedIndex].text.toLowerCase();
        if (selectedGenreValue === "tirinha" || selectedGenreValue === "ilustração") {
            askForIllustration.style.display = "none";
        } else {
            askForIllustration.style.display = "block";
        }
        if (selectedSectionValue === "ilustrações") {
            askForIllustration.style.display = "none";
        }
    }

    genreSelect.addEventListener('change', toggleIllustrationMenu);
    sectionSelect.addEventListener('change', toggleIllustrationMenu);

    toggleIllustrationMenu();
});

document.getElementById("submit-button").addEventListener("click", function(event) {
    const imageInput = document.getElementById("id_image");
    const imageFile = imageInput.files.length;

    if (imageFile === 0) {
        event.preventDefault();

        const errorMessage = document.getElementById("image-error-message");
        errorMessage.style.display = "block";
    } else {
        const errorMessage = document.getElementById("image-error-message");
        errorMessage.style.display = "none";
    }
});
