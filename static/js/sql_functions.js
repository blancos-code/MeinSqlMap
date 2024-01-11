function afficherPopup(index,indexRecherche,recherche,page_depart,nb_site,isModifying) {
    var popup = document.getElementById("popup"+index);
    var rechercheEl = document.getElementById("inputTextHistorique");
    var startPageEl = document.getElementById("inputNumberHistorique");
    var idHistoriqueEl = document.getElementById("idHistorique");
    var nbRequeteEL = document.getElementById("inputNumberRequete");
    var submitButton = document.getElementById("submitButton");
    var modifyButton = document.getElementById("modifyButton");


    if(recherche){
      rechercheEl.value = recherche;
    }
    startPageEl.value = page_depart;
    nbRequeteEL.value = nb_site;
    idHistoriqueEl.value = indexRecherche;

    if (isModifying) {
      submitButton.style.display = "none"; // Cacher le bouton "Envoyer"
      submitButton.disabled = true;
      modifyButton.style.display = "block"; // Afficher le bouton "Modifier"
      modifyButton.disabled = false;
    } else {
      submitButton.style.display = "block"; // Afficher le bouton "Envoyer"
      submitButton.disabled = false;
      modifyButton.style.display = "none"; // Cacher le bouton "Modifier"
      modifyButton.disabled = true;
    }
    
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

function editHistorique() {
  // on ouvre le formulaire
  var idRecherche = document.getElementById("idHistorique").value;
  var rechercheText = document.getElementById("inputTextHistorique").value;
  var pageDepart = document.getElementById("inputNumberHistorique").value;
  var nbRequete = document.getElementById("inputNumberRequete").value;

  // Créer un objet JSON avec les données soumises
  var jsonData = {
    idHistorique: idRecherche,
    inputTextHistorique: rechercheText,
    inputNumberHistorique: pageDepart,
    inputNumberRequete: nbRequete
  };

  // Appeler l'API avec les données soumises
  fetch("/sql_edit_historique", {
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
  fermerPopup(2);
  window.location.reload();
}

function deleteHistorique(id) {

// Appeler l'API avec les données soumises
  fetch("/sql/history/delete/" + id, {
      method: "POST",

  }).then(r => {
        console.log(r);
        window.location.reload();
  });
}