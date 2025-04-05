
const joursSemaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"];
const progressBar = document.getElementById("progressBar");
const boutonNext = document.querySelector(".nextDay");
const boutonPrec = document.querySelector(".prevDay");

let jourIndex = localStorage.getItem('jourIndex') ? parseInt(localStorage.getItem('jourIndex')) : 0;

// Initialisation de la barre de progression
function updateProgressBar() {
    const percentage = (jourIndex + 1) * 14;
    progressBar.style.width = `${percentage}%`;
    progressBar.textContent = `${percentage}%`;
}


function changerJour() {
    const titre = document.querySelector("h2");
    const inputJour = document.querySelector("#jourNom");

    if (titre && inputJour) {
        titre.textContent = joursSemaine[jourIndex];
        inputJour.value = joursSemaine[jourIndex];
        updateProgressBar();
        if (jourIndex === 6) {
            boutonNext.textContent = "Générer le programme";
            boutonNext.id = "generateProgram";
        } else {
            boutonNext.textContent = "Jour Suivant";
            boutonNext.id = "nextDay";
        }

    }
}
document.addEventListener("DOMContentLoaded", Day());

function Day(){
const boutonNext = document.querySelector(".nextDay");
const boutonPrec = document.querySelector(".prevDay");
    changerJour();
    if (boutonNext) {
        boutonNext.addEventListener("click", function () {

            if (jourIndex < 6) {
                jourIndex++;
        localStorage.setItem('jourIndex', jourIndex);
           changerJour();
            } else {
                  // Rediriger vers la vue Django qui génère le programme
                window.location.href = "/generer_programme/";
            }

        });
    }
     if (boutonPrec) {
        boutonPrec.addEventListener("click", function () {
          //  jourIndex = (jourIndex + 1) % joursSemaine.length;
            if (jourIndex > 0) {
                jourIndex--;
        localStorage.setItem('jourIndex', jourIndex);
            }
            changerJour();
        });
    }
}

 function hideMessage(id) {
    setTimeout(function() {
      const message = document.getElementById(id);
      if (message) {
        message.style.display = 'none';
      }
    }, 3000);
  }
  if (document.getElementById('success-message')) {
    hideMessage('success-message');
  }
  if (document.getElementById('error-message')) {
    hideMessage('error-message');
  }
