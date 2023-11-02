document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
      // Ici, vous pourriez envoyer les URLs à scanner au serveur.
      // Cependant, dans ce cas, le serveur démarre les scans dans la route /results.
    });

    socket.on('console_output', function(data) {
    var index = data.index;
    var url = data.url;
    var output = data.data.replace(/\n/g, '<br>');

    var a = document.createElement('a');
    a.href = url;

    var domain = a.hostname;

    var consoleElement = document.getElementById('console-' + index);
    var urlElement = document.getElementById('url-' + index);

    if (urlElement) {
        urlElement.innerHTML = domain; // Affichez le nom de domaine au lieu de l'URL complète
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