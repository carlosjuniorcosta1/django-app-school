
const textBox = document.getElementById('textBox');
const undoButton = document.getElementById('undoButton')
const textBoxButton = document.getElementById('textBoxButton');
const downloadButton = document.getElementById('downloadButton');
let currentFontSize = 16;


img.onload = function() {
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height); }



let isDragging = false;
let offsetX, offsetY;

let currentColor = colorPicker.value; // 

colorPicker.addEventListener('input', (event) => {
  currentColor = event.target.value; //
});

increaseFontButton.addEventListener('click', function() {
    currentFontSize += 2; 
    ctx.font = `${currentFontSize}px Arial`; 
    textBox.style.fontSize = `${currentFontSize}px`;
});

let textEntries = []

function showtextBox(x, y) {
  textBox.style.left = `${canvas.offsetLeft + x}px`;
  textBox.style.top = `${canvas.offsetTop + y}px`;
  textBox.style.display = "block";
  textBox.focus();
}

function addTextToCanvas() {
  const text = textBox.value;
  const x = parseInt(textBox.style.left) - canvas.offsetLeft;
  const y = parseInt(textBox.style.top) - canvas.offsetTop;

  textEntries.push({text,  x, y, color: currentColor, fontSize: currentFontSize})

ctx.font = `${currentFontSize}px Arial`
  ctx.fillStyle = currentColor; 
  ctx.fillText(text, x, y);

  textBox.value = ""; 
  textBox.style.display = "none"; 
}

function redrawCanvas(){

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);





    textEntries.forEach(entry => {
        ctx.font = `${entry.fontSize}px Arial`
        ctx.fillStyle = entry.color,
        ctx.fillText(entry.text, entry.x, entry.y)
    })
    

}
canvas.addEventListener("click", function(event) {
  const x = event.offsetX;
  const y = event.offsetY;
  showtextBox(x, y);
});

document.addEventListener('mousedown', function(event) {
  if (event.target === textBox) {
    isDragging = true;
    offsetX = event.offsetX;
    offsetY = event.offsetY;
  }
});

document.addEventListener('mousemove', function(event) {
  if (isDragging) {
    const x = event.pageX - offsetX;
    const y = event.pageY - offsetY;
    textBox.style.left = `${x}px`;
    textBox.style.top = `${y}px`;
  }
});

document.addEventListener('mouseup', function() {
  isDragging = false;
});

textBox.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    addTextToCanvas();
  }
});

undoButton.addEventListener('click', function(){
    if(textEntries.length > 0) {
        textEntries.pop();
        redrawCanvas()
    }
})

textBoxButton.addEventListener('click', function() {
    if (textBox.style.display === "none") {
      showtextBox(50, 50); 
    } else {
      textBox.style.display = "none"
    }
  });

  downloadButton.addEventListener('click', function() {
    const link = document.createElement('a');
    link.download = 'canvas-image.png'; 
    link.href = canvas.toDataURL(); 
    link.click(); // 
  });

    ctx.fillRect(0, 0, canvas.width, canvas.height); 


</script>