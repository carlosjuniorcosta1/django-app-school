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
    const previewContainer = document.getElementById('preview-container'); // Contêiner que engloba o preview

    // Preview dos ingredientes e modo de preparo
    const ingredientsContainer = document.getElementById('ingredients-container');
    const preparationContainer = document.getElementById('preparation-container');
    const ingredientsPreview = document.getElementById('ingredients-preview');
    const preparationPreview = document.getElementById('preparation-preview');

    titleInput.addEventListener('input', function () {
        previewTitle.textContent = titleInput.value;
    });

    subtitleInput.addEventListener('input', function () {
        previewSubtitle.textContent = subtitleInput.value;
    });

    mainTextInput.addEventListener('input', function () {
        updatePreviewMainText();
        updateRecipePreview(); // Atualiza os previews
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

    function updatePreviewMainText() {
        const paragraphs = mainTextInput.value.split('\n');
        previewMainText.innerHTML = paragraphs.map(paragraph => `<p class="mb-1">${paragraph}</p>`).join('');
    }

    function updateRecipePreview() {
        const text = mainTextInput.value;
        const ingredientsMatch = text.match(/Ingredientes:(.*?)(Modo de preparo:|$)/s);
        const preparationMatch = text.match(/Modo de preparo:(.*)/s);

        // Atualizar ingredientes
        if (ingredientsMatch) {
            const ingredients = ingredientsMatch[1].trim().split('\n').filter(line => line.trim() !== "");
            ingredientsPreview.innerHTML = ingredients.map(ingredient => `<li>${ingredient}</li>`).join('');
            ingredientsContainer.style.display = 'block';
        } else {
            ingredientsContainer.style.display = 'none';
        }

        // Atualizar modo de preparo
        if (preparationMatch) {
            const preparation = preparationMatch[1].trim().split('\n').filter(line => line.trim() !== "");
            preparationPreview.innerHTML = preparation.map(step => `<li>${step}</li>`).join('');
            preparationContainer.style.display = 'block';
        } else {
            preparationContainer.style.display = 'none';
        }
    }

    // Sincronizar os campos de gênero textual e seção
    const genreSelect = document.getElementById('id_textual_genre');
    const sectionSelect = document.getElementById('id_section_name');

    function syncFields() {
        const selectedGenre = genreSelect.options[genreSelect.selectedIndex].text.toLowerCase();

        // Ajustar seção de acordo com o gênero
        if (selectedGenre === 'artigo') {
            selectSectionByName('opinião');
            showPreview(); // Mostra o preview
        } else if (['conto', 'fanfic'].includes(selectedGenre)) {
            selectSectionByName('literatura');
            showPreview(); // Mostra o preview
        } else if (['tirinha', 'ilustração'].includes(selectedGenre)) {
            selectSectionByName('ilustrações');
            showPreview(); // Mostra o preview
        } else if (selectedGenre === 'receita') {
            selectSectionByName('comida');
            insertRecipeTemplate();
            hidePreview(); // Oculta o preview de título, subtítulo, nome e texto
        }
    }

    function selectSectionByName(sectionName) {
        for (let i = 0; i < sectionSelect.options.length; i++) {
            if (sectionSelect.options[i].text.toLowerCase() === sectionName) {
                sectionSelect.selectedIndex = i;
                break;
            }
        }
    }

    function insertRecipeTemplate() {
        if (mainTextInput.value.trim() === '') {
            mainTextInput.value = "Ingredientes:\n \n \nModo de preparo:\n \n \n \n";
        }
    }

    function hidePreview() {
        // Oculta título, subtítulo, nome e texto, mas mantém a imagem
        previewSubtitle.style.display = 'none';
        previewMainText.style.display = 'none';
    }

    function showPreview() {
        // Mostra título, subtítulo, nome e texto novamente
        previewSubtitle.style.display = 'block';
        previewMainText.style.display = 'block';
    }

    genreSelect.addEventListener('change', syncFields);
    sectionSelect.addEventListener('change', syncFields);
});


document.addEventListener("DOMContentLoaded", function () {
    const titleInput = document.getElementById('id_title');
    const previewTitle = document.getElementById('preview-title');

    function capitalizeFirstLetter(text) {
        if (text.length === 0) return text;
        return text.charAt(0).toUpperCase() + text.slice(1);
    }

    titleInput.addEventListener('input', function () {
        const capitalizedTitle = capitalizeFirstLetter(titleInput.value);
        previewTitle.textContent = capitalizedTitle;
        titleInput.value = capitalizedTitle; 
    });
});
