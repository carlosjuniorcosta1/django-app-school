document.addEventListener("DOMContentLoaded", function(){
    setTimeout(function () {
        var alert = document.querySelector('.alert')
        if (alert) {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";
            setTimeout(function() {
                alert.remove();

            }, 500);
        }
    }, 1500);

});