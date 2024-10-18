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

    function addChronicleOption() {
        let optionExists = false;
        for (let i = 0; i < genreSelect.options.length; i++) {
            if (genreSelect.options[i].text.toLowerCase() === 'crônica') {
                optionExists = true;
                break;
            }
        }
        if (!optionExists) {
            const option = new Option('Crônica', 'crônica');
            genreSelect.add(option);
        }
    }

    function removeChronicleOption() {
        for (let i = 0; i < genreSelect.options.length; i++) {
            if (genreSelect.options[i].text.toLowerCase() === 'crônica') {
                genreSelect.remove(i);
                break;
            }
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

    function selectGenreByName(genreName) {
        for (let i = 0; i < genreSelect.options.length; i++) {
            if (genreSelect.options[i].text.toLowerCase() === genreName) {
                genreSelect.selectedIndex = i;
                break;
            }
        }
    }

    function insertRecipeTemplate() {
        if (mainTextInput.value.trim() === '') {
            mainTextInput.value = "Ingredientes:\n \n \nModo de preparo:\n \n \n \n";
        }
    }

    function toggleHideTextField() {
        const selectedGenre = genreSelect.options[genreSelect.selectedIndex].text.toLowerCase();
        const selectedSection = sectionSelect.options[sectionSelect.selectedIndex].text.toLowerCase();

        if (selectedGenre === 'tirinha' || selectedGenre === 'ilustração') {
            mainTextField.style.display = 'none';
            subtitleSelect.style.display = 'none';
        } else {
            mainTextField.style.display = 'block';
            subtitleSelect.style.display = 'block';
        }

        if (selectedSection === 'ilustrações') {
            mainTextField.style.display = 'none';
            subtitleSelect.style.display = 'none';

            genreSelect.innerHTML = ''; 
            allowedGenresForIllustrations.forEach(function (genre) {
                allGenres.forEach(function (option) {
                    if (option.text.toLowerCase() === genre) {
                        genreSelect.appendChild(option); 
                    }
                });
            });
        } else {
            genreSelect.innerHTML = ''; 
            allGenres.forEach(function (option) {
                genreSelect.appendChild(option); 
            });
            mainTextField.style.display = 'block';
            subtitleSelect.style.display = 'block';
        }
    }

    if (artistAtt == 'False') {
        textualGenreSelect.addEventListener('change', function () {
            const textTextualGenre = textualGenreSelect.options[textualGenreSelect.selectedIndex].text;
            if (textTextualGenre === "Ilustração" || textTextualGenre === "Tirinha") {
                selectedGenre.innerHTML = "Você ainda não tem permissão de ilustrador. Solicite-a ao administrador via email e mostre seu trabalho antes.";
                selectedGenre.style.display = "block";
                for (let i = 0; i < hideFields.length; i++) {
                    hideFields[i].style.display = 'none';
                }
                textualGenreSelect.selectedIndex = 0; 
            } else {
                selectedGenre.style.display = "none";
                for (let i = 0; i < hideFields.length; i++) {
                    hideFields[i].style.display = "block";
                }
            }
        });
    }

    titleInput.addEventListener('input', function () {
        const capitalizedTitle = capitalizeFirstLetter(titleInput.value);
        previewTitle.textContent = capitalizedTitle;
        titleInput.value = capitalizedTitle; 
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
});


document.getElementById("submit-button").addEventListener("click", function(event) {
    const imageInput = document.getElementById("id_image");
    const imageFile = imageInput.files.length; // Verifica se há um arquivo

    // Se não houver arquivo
    if (imageFile === 0) {
        event.preventDefault(); // Impede o envio do formulário
        
        // Mostra a mensagem de erro
        const errorMessage = document.getElementById("image-error-message");
        errorMessage.style.display = "block"; // Torna a mensagem visível
    } else {
        // Se houver imagem, esconde a mensagem de erro (caso tenha sido exibida anteriormente)
        const errorMessage = document.getElementById("image-error-message");
        errorMessage.style.display = "none"; // Esconde a mensagem de erro
    }
});
