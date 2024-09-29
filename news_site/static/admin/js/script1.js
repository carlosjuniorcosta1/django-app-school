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

    function updatePreviewMainText() {
        const paragraphs = mainTextInput.value.split('\n');
        previewMainText.innerHTML = paragraphs.map(paragraph => `<p class="mb-1">${paragraph}</p>`).join('');
    }

    function updateRecipePreview() {
        const text = mainTextInput.value;
        const ingredientsMatch = text.match(/Ingredientes:(.*?)(Modo de preparo:|$)/s);
        const preparationMatch = text.match(/Modo de preparo:(.*)/s);

        if (ingredientsMatch) {
            const ingredients = ingredientsMatch[1].trim().split('\n').filter(line => line.trim() !== "");
            ingredientsPreview.innerHTML = ingredients.map(ingredient => `<li>${ingredient}</li>`).join('');
            ingredientsContainer.style.display = 'block';
        } else {
            ingredientsContainer.style.display = 'none';
        }

        if (preparationMatch) {
            const preparation = preparationMatch[1].trim().split('\n').filter(line => line.trim() !== "");
            preparationPreview.innerHTML = preparation.map(step => `<li>${step}</li>`).join('');
            preparationContainer.style.display = 'block';
        } else {
            preparationContainer.style.display = 'none';
        }
    }

    const genreSelect = document.getElementById('id_textual_genre');
    const sectionSelect = document.getElementById('id_section_name');

    function syncFields() {
        const selectedGenre = genreSelect.options[genreSelect.selectedIndex].text.toLowerCase();

        if (selectedGenre === 'artigo') {
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
        previewSubtitle.style.display = 'none';
        previewMainText.style.display = 'none';
    }

    function showPreview() {
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

document.addEventListener('DOMContentLoaded', function() {
    var idArtist = document.getElementById('idArtist')
    var artistAtt = idArtist.getAttribute('data-is-artist')
    var textualGenreSelect = document.getElementById('id_textual_genre');
    var selectedGenre = document.getElementById('selected-genre')
    var hideFields = document.getElementsByClassName('hide-ilustrator')

    console.log(artistAtt)
    if(artistAtt == 'False'){
        textualGenreSelect.addEventListener('change', function(){
            var textTextualGenre = textualGenreSelect.options[textualGenreSelect.selectedIndex].text
        if(textTextualGenre == "Ilustração"|| textTextualGenre == "Tirinha"){
                selectedGenre.innerHTML = "Você ainda não tem permissão de ilustrador. Solicite-a ao administrador via email e mostre seu trabalho antes."
                selectedGenre.style.display = "block"
                for(var i = 0; i < hideFields.length; i++){
                    hideFields[i].style.display =  'none'
                }
                textualGenreSelect.selectedIndex = 0; 
            }
            else {
                selectedGenre.style.display = "none"
                for(var i=0; i < hideFields.length; i++){
                    hideFields[i].style.display = "block"
                }
            }
        } )       

    }  
});