document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM chargé !")
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
      // Ici, vous pourriez envoyer les URLs à scanner au serveur.
      // Cependant, dans ce cas, le serveur démarre les scans dans la route /results.
    });

    socket.on('console_output', function(data) {
        var index = data.index;
        var url = data.url;
        var output = data.data.replace(/\n/g, '<br>'); // Remplacez les sauts de ligne par des balises <br>

        // Trouvez l'élément pour afficher la console de cette URL spécifique
        var consoleElement = document.getElementById('console-' + index);
        var urlElement = document.getElementById('url-' + index);

        if (urlElement) {
            urlElement.innerHTML = url;
            urlElement.href = url;
        }
        if (consoleElement) {
            var preElement = consoleElement.querySelector('pre');
            // Ajoutez la nouvelle ligne de sortie à la console
            preElement.innerHTML += output + '<br>'; // Ajoutez un saut de ligne après chaque sortie

            // Faites défiler jusqu'en bas pour voir la dernière ligne
            preElement.scrollTop = preElement.scrollHeight;
        }
    });
});