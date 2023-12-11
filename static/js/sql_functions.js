function afficherPopup(index) {
    var popup = document.getElementById("popup"+index);
    popup.style.display = "flex";
}
  
function fermerPopup(index) {
    var popup = document.getElementById("popup"+index);
    popup.style.display = "none";
}


function insertSite() {
  var inputText = document.getElementById("inputTextSite").value;

  // Créer un objet JSON avec les données soumises
  var jsonData = {
      user_input: inputText,
  };

  // Appeler l'API avec les données soumises
  fetch("/sql_add_site", {
      method: "POST",
      body: JSON.stringify(jsonData),
      headers: {
      "Content-Type": "application/json"
      }
  })
  .then(response => response.json())
  .then(data => {
      // Traiter ici la réponse de l'API
      console.log(data.result);
  })
  .catch(error => {
      console.error("Une erreur s'est produite:", error);
  });
}

function insertHistorique() {
    var inputText = document.getElementById("inputTextHistorique").value;
    var inputNumber1 = document.getElementById("inputNumberHistorique").value;
    var inputNumber2 = document.getElementById("inputNumberRequete").value;

    // Créer un objet JSON avec les données soumises
    var jsonData = {
      inputTextHistorique: inputText,
      inputNumberHistorique: inputNumber1,
      inputNumberRequete: inputNumber2
    };

    // Appeler l'API avec les données soumises
    fetch("/sql_add_historique", {
      method: "POST",
      body: JSON.stringify(jsonData),
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(response => response.json())
    .then(data => {
      // Traiter ici la réponse de l'API
      console.log(data.result);
    })
    .catch(error => {
      console.error("Une erreur s'est produite:", error);
    });
  }