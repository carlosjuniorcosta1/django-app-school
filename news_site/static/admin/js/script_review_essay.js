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