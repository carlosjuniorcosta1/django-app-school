document.getElementById('essay-form').addEventListener('submit', function(event){
    event.preventDefault()

    const confirmMessage = document.getElementById('confirmation-message')
    confirmMessage.innerHTML = "Sua redação foi enviada para correção!"
    confirmMessage.style.display = 'block'
    setTimeout(function(){
        confirmMessage.style.display = 'none'    
    
        document.getElementById('essay-form').submit()
    }, 6000);
})


  const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const img = new Image();
    img.src = "{{ essay.essay_image.url }}"; // Carrega a imagem da redação

    img.onload = function() {
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height); // Desenha a imagem no canvas
    };

    // Variáveis de controle
    let isDrawing = false;
    let isTextMode = false;
    let isDrawingMode = false;
    let isDraggingTextBox = false;
    let selectedTextBox = null;
    let offsetX = 0, offsetY = 0;
    let textBoxes = [];
    let actions = [];
    let currentPath = [];

    // Função para calcular a largura do texto e ajustar o tamanho da caixa de texto
    function adjustTextareaWidth(textBox) {
        const span = document.createElement('span');
        span.style.font = '20px Arial';
        span.style.visibility = 'hidden';
        span.style.whiteSpace = 'nowrap';
        span.style.padding = '5px'
        span.textContent = textBox.value;
        document.body.appendChild(span);

        const textWidth = span.offsetWidth;
        textBox.style.width = textWidth + 'px';

        document.body.removeChild(span);
    }

    // Evento para criar a caixa de texto
    canvas.addEventListener('mousedown', function(e) {
        if (isTextMode) {
            isDraggingTextBox = true;

            const textBox = document.createElement('textarea');
            textBox.style.position = 'absolute';
            textBox.style.left = e.pageX + 'px';
            textBox.style.top = e.pageY + 'px';
            textBox.style.height = '30px';
            textBox.style.font = '20px Arial';
            textBox.style.color = 'red';
            textBox.style.background = 'transparent';
            textBox.style.border = '1px dashed #000';
            textBox.style.whiteSpace = 'nowrap';
            textBox.style.resize = 'none'; // Impedir redimensionamento manual
            textBox.style.overflow = 'hidden';
            document.body.appendChild(textBox);

            offsetX = e.pageX - canvas.offsetLeft;
            offsetY = e.pageY - canvas.offsetTop;

            textBoxes.push(textBox);

            actions.push({ type: 'add', element: textBox });

            textBox.addEventListener('mousedown', function(event) {
                selectedTextBox = textBox;
                offsetX = event.pageX - selectedTextBox.offsetLeft;
                offsetY = event.pageY - selectedTextBox.offsetTop;
                isDraggingTextBox = true;
            });

            document.addEventListener('mouseup', function() {
                isDraggingTextBox = false;
            });

            document.addEventListener('mousemove', function(event) {
                if (isDraggingTextBox && selectedTextBox) {
                    selectedTextBox.style.left = (event.pageX - offsetX) + 'px';
                    selectedTextBox.style.top = (event.pageY - offsetY) + 'px';
                }
            });

            // Aumentar a largura da caixa de texto conforme a digitação
            textBox.addEventListener('input', function() {
                adjustTextareaWidth(textBox);
            });

            // Adicionar o texto no canvas ao pressionar Enter
            textBox.addEventListener('keydown', function(event) {
                if (event.key === 'Enter') {
                    event.preventDefault();
                    const text = textBox.value;
                    const x = parseInt(textBox.style.left, 10) - canvas.offsetLeft;
                    const y = parseInt(textBox.style.top, 10) - canvas.offsetTop;

                    // Adicionar o texto no canvas
                    ctx.font = '20px Arial';
                    ctx.fillStyle = 'red';
                    ctx.fillText(text, x, y);

                    document.body.removeChild(textBox);

                    actions.push({ type: 'text', text, x, y });
                }
            });
        } else if (isDrawingMode) {
            isDrawing = true;
            currentPath = [{ x: e.offsetX, y: e.offsetY }];
            ctx.beginPath();
            ctx.moveTo(e.offsetX, e.offsetY);
        }
    });

    canvas.addEventListener('mousemove', function(e) {
        if (isDrawing && isDrawingMode) {
            ctx.lineTo(e.offsetX, e.offsetY);
            ctx.strokeStyle = 'red';
            ctx.lineWidth = 3;
            ctx.stroke();

            currentPath.push({ x: e.offsetX, y: e.offsetY });
        }
    });

    document.addEventListener('mouseup', function() {
        if (isDrawing) {
            isDrawing = false;
            actions.push({ type: 'draw', path: currentPath.slice() });
        }
    });

    document.getElementById('btn-text').addEventListener('click', function() {
        isTextMode = true;
        isDrawingMode = false;
    });

    document.getElementById('btn-draw').addEventListener('click', function() {
        isDrawingMode = true;
        isTextMode = false;
    });

    document.getElementById('btn-clear').addEventListener('click', function() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

        textBoxes.forEach(function(box) {
            document.body.removeChild(box);
        });
        textBoxes = [];
        actions = [];
    });

    document.getElementById('btn-save').addEventListener('click', function() {
        const dataURL = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.href = dataURL;
        link.download = 'correcao_redacao.png';
        link.click();
    });

    document.getElementById('btn-undo').addEventListener('click', function() {
        if (actions.length > 0) {
            const lastAction = actions.pop();

            if (lastAction.type === 'add') {
                document.body.removeChild(lastAction.element);
                textBoxes.pop();
            } else if (lastAction.type === 'draw') {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                actions.forEach(function(action) {
                    if (action.type === 'draw') {
                        ctx.beginPath();
                        ctx.moveTo(action.path[0].x, action.path[0].y);

                        action.path.forEach(function(point) {
                            ctx.lineTo(point.x, point.y);
                        });

                        ctx.stroke();
                    } else if (action.type === 'text') {
                        ctx.font = '20px Arial';
                        ctx.fillStyle = 'red';
                        ctx.fillText(action.text, action.x, action.y);
                    }
                });
            }
        }
    });
