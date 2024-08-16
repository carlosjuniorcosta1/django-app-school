document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("filtrar").addEventListener('click', function() {
        var materia = document.getElementById('materias').value;
        var ano = document.getElementById('anos').value;
        
        var searchP = new URLSearchParams(window.location.search);
        searchP.set('materia', materia);
        searchP.set('ano', ano);
        window.location.search = searchP.toString();
    });
});
