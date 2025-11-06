/**
 * Calculateur FALC ou Langage Clair
 * Source: https://com-access.fr/falc-ou-lc/
 *
 * Ce script détermine si un document doit être rédigé en FALC ou en Langage Clair
 * en fonction des réponses à 10 questions sur le public cible et le document.
 *
 * RÈGLES DE CALCUL:
 * - Une fois le FALC recommandé, la recommandation ne change plus
 * - Les questions 1, 7, 8, 9, 10 ne changent pas la recommandation (collecte d'info uniquement)
 * - Les questions 2-6 peuvent déclencher une recommandation FALC ou LC avec avertissement
 */

/**
 * Place le focus sur la section suivante du formulaire
 * @param {string} idSection - L'ID de la section à focaliser
 */
function focusSurSectionSuivante(idSection) {
  const section = document.getElementById(idSection);
  if (section) {
    // Trouver le premier élément interactif (input, select, button, etc.)
    const focusable = section.querySelector('input, select, button, textarea, fieldset');
    if (focusable) {
      focusable.focus();
    }
  }
}

/**
 * Valide une étape du formulaire
 * @param {string} cible - Le nom de la question/cible
 */
function validerEtape(cible) {
  const radios = document.getElementsByName(cible);
  let reponse = "";
  for (let radio of radios) {
    if (radio.checked) {
      reponse = radio.value;
      break;
    }
  }

  if (!reponse) {
    alert("Veuillez sélectionner une réponse avant de continuer.");
    return;
  }

  gererReponse(cible, reponse);
}

/**
 * Gère la réponse d'une question et détermine la recommandation
 * @param {string} cible - Le nom de la question
 * @param {string} reponse - La réponse sélectionnée
 *
 * LOGIQUE DE DÉCISION:
 * Q1 (organisme): Collecte d'info uniquement
 * Q2 (agee): "Oui, en majorité" -> LC avec peut-être FALC
 * Q3 (adulte): "Oui, en majorité" -> FALC (décision finale)
 * Q4 (etranger): "Non, ce n'est pas la majorité" -> LC avec peut-être FALC
 * Q5 (handicap): "Oui, en majorité" -> FALC (décision finale)
 * Q6 (autonomie): "Non, ce n'est pas la majorité" -> FALC (décision finale)
 * Q7-10: Collecte d'info uniquement
 */
function gererReponse(cible, reponse) {
  const resultat = document.getElementById("resultat");
  // Vérifier si le texte actuel est "Nous vous conseillons de rédiger votre document en FALC."
  const currentResult = resultat.textContent;

  // QUESTION 1: Type d'organisme (collecte d'info uniquement)
  if (cible === "organisme") {
    if (reponse) {
      const radios = document.getElementsByName('organisme');
      let resume = "1 - Votre organisme : ";

      // Vérifier quelle option radio est sélectionnée
      let optionChoisie = "";
      for (let radio of radios) {
        if (radio.checked) {
          optionChoisie = radio.value;
          break;
        }
      }
      resume += optionChoisie;
      // Afficher le résumé dans la page
      document.getElementById('resume').textContent = resume;

      document.getElementById("cible-organisme").style.display = "none";
      resultat.style.display = "none";
      // Afficher la cible "agee"
      document.getElementById("cible-agee").style.display = "block";
      focusSurSectionSuivante("cible-agee");
    }
  }

  // QUESTION 2: Public âgé de 70 ans ou plus
  // RÈGLE: "Oui, en majorité" -> LC avec avertissement FALC possible
  if (cible === "agee") {
    const radios = document.getElementsByName('agee');
    let resume2 = "2 - Votre cible est âgée : ";

    let optionChoisie2 = "";
    for (let radio of radios) {
      if (radio.checked) {
        optionChoisie2 = radio.value;
        break;
      }
    }
    resume2 += optionChoisie2;
    document.getElementById('resume2').textContent = resume2;
    document.getElementById("cible-agee").style.display = "none";

    if (reponse === "Oui, en majorité") {
      // AVERTISSEMENT: LC recommandé mais FALC peut être envisagé
      resultat.textContent = "Nous vous conseillons de rédiger votre document en Langage Clair, mais il faudra peut-être envisager le FALC.";
      document.getElementById("cible-adulte").style.display = "block";
    } else {
      resultat.textContent = "Nous vous conseillons de rédiger votre document en Langage Clair.";
      document.getElementById("cible-agee").style.display = "none";
      document.getElementById("cible-adulte").style.display = "block";
      focusSurSectionSuivante("cible-adulte");
    }
  }

  // QUESTION 3: Niveau scolaire collège (≤ 4ème)
  // RÈGLE: "Oui, en majorité" -> FALC (décision finale, ne change plus)
  if (cible === "adulte") {
    const radios = document.getElementsByName('adulte');
    let resume3 = "3 - Votre cible a un niveau collège : ";

    let optionChoisie3 = "";
    for (let radio of radios) {
      if (radio.checked) {
        optionChoisie3 = radio.value;
        break;
      }
    }
    resume3 += optionChoisie3;
    document.getElementById('resume3').textContent = resume3;
    document.getElementById("cible-adulte").style.display = "none";

    // Si FALC n'a pas déjà été recommandé, vérifier cette question
    if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
      if (reponse === "Oui, en majorité") {
        // DÉCISION FINALE: FALC
        resultat.textContent = "Nous vous conseillons de rédiger votre document en FALC.";
      }
      document.getElementById("cible-etranger").style.display = "block";
    } else {
      document.getElementById("cible-adulte").style.display = "none";
      document.getElementById("cible-etranger").style.display = "block";
      focusSurSectionSuivante("cible-etranger");
    }
  }

  // QUESTION 4: Maîtrise de la langue française
  // RÈGLE: "Non, ce n'est pas la majorité" -> LC avec avertissement FALC possible
  if (cible === "etranger") {
    const radios = document.getElementsByName('etranger');
    let resume4 = "4 - Votre cible maitrise la langue française : ";

    let optionChoisie4 = "";
    for (let radio of radios) {
      if (radio.checked) {
        optionChoisie4 = radio.value;
        break;
      }
    }
    resume4 += optionChoisie4;
    document.getElementById('resume4').textContent = resume4;
    document.getElementById("cible-etranger").style.display = "none";

    // Si FALC n'a pas déjà été recommandé, vérifier cette question
    if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
      if (reponse === "Non, ce n'est pas la majorité") {
        // AVERTISSEMENT: LC recommandé mais FALC peut être envisagé
        resultat.textContent = "Nous vous conseillons de rédiger votre document en Langage Clair, mais il faudra peut-être envisager le FALC.";
      }
      document.getElementById("cible-handicap").style.display = "block";
    } else {
      document.getElementById("cible-etranger").style.display = "none";
      document.getElementById("cible-handicap").style.display = "block";
      focusSurSectionSuivante("cible-handicap");
    }
  }

  // QUESTION 5: Handicap mental/psychique/cognitif
  // RÈGLE: "Oui, en majorité" -> FALC (décision finale, ne change plus)
  if (cible === "handicap") {
    const radios = document.getElementsByName('handicap');
    let resume5 = "5 - Votre cible est en situation de handicap  : ";

    let optionChoisie5 = "";
    for (let radio of radios) {
      if (radio.checked) {
        optionChoisie5 = radio.value;
        break;
      }
    }
    resume5 += optionChoisie5;
    document.getElementById('resume5').textContent = resume5;
    document.getElementById("cible-handicap").style.display = "none";

    // Si FALC n'a pas déjà été recommandé, vérifier cette question
    if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
      if (reponse === "Oui, en majorité") {
        // DÉCISION FINALE: FALC
        resultat.textContent = "Nous vous conseillons de rédiger votre document en FALC.";
      }
      document.getElementById("cible-autonomie").style.display = "block";
    } else {
      document.getElementById("cible-handicap").style.display = "none";
      document.getElementById("cible-autonomie").style.display = "block";
      focusSurSectionSuivante("cible-autonomie");
    }
  }

  // QUESTION 6: Autonomie de lecture
  // RÈGLE: "Non, ce n'est pas la majorité" -> FALC (décision finale, ne change plus)
  if (cible === "autonomie") {
    const radios = document.getElementsByName('autonomie');
    let resume6 = "6 - Votre cible est autonome pour lire : ";

    let optionChoisie6 = "";
    for (let radio of radios) {
      if (radio.checked) {
        optionChoisie6 = radio.value;
        break;
      }
    }
    resume6 += optionChoisie6;
    document.getElementById('resume6').textContent = resume6;
    document.getElementById("cible-autonomie").style.display = "none";

    // Si FALC n'a pas déjà été recommandé, vérifier cette question
    if (currentResult !== "Nous vous conseillons de rédiger votre document en FALC.") {
      if (reponse === "Non, ce n'est pas la majorité") {
        // DÉCISION FINALE: FALC
        resultat.textContent = "Nous vous conseillons de rédiger votre document en FALC.";
      }
      document.getElementById("cible-connaissance").style.display = "block";
    } else {
      document.getElementById("cible-autonomie").style.display = "none";
      document.getElementById("cible-connaissance").style.display = "block";
      focusSurSectionSuivante("cible-connaissance");
    }
  }

  // QUESTION 7: Connaissance du sujet (collecte d'info uniquement)
  if (cible === "connaissance") {
    if (reponse) {
      const radios = document.getElementsByName('connaissance');
      let resume7 = "7 - Votre cible connait le sujet : ";

      let optionChoisie7 = "";
      for (let radio of radios) {
        if (radio.checked) {
          optionChoisie7 = radio.value;
          break;
        }
      }
      resume7 += optionChoisie7;
      document.getElementById('resume7').textContent = resume7;
      document.getElementById("cible-connaissance").style.display = "none";
      document.getElementById("cible-taille").style.display = "block";
      focusSurSectionSuivante("cible-taille");
    }
  }

  // QUESTION 8: Taille du document (collecte d'info uniquement)
  if (cible === "taille") {
    if (reponse) {
      const radios = document.getElementsByName('taille');
      let resume8 = "8 - Votre document aura : ";

      let optionChoisie8 = "";
      for (let radio of radios) {
        if (radio.checked) {
          optionChoisie8 = radio.value;
          break;
        }
      }
      resume8 += optionChoisie8;
      document.getElementById('resume8').textContent = resume8;
      document.getElementById("cible-taille").style.display = "none";
      document.getElementById("cible-publication").style.display = "block";
      focusSurSectionSuivante("cible-publication");
    }
  }

  // QUESTION 9: Mode de publication (collecte d'info uniquement, choix multiples)
  if (cible === "publication") {
    if (reponse) {
      const checkboxes = document.querySelectorAll('input[name="publication"]:checked');
      let resume9 = "9 - Votre document sera publié sur : ";

      // Récupérer toutes les valeurs sélectionnées
      const optionsChoisies = Array.from(checkboxes).map(cb => cb.value);

      // Joindre les valeurs avec des virgules
      resume9 += optionsChoisies.join(', ');

      document.getElementById('resume9').textContent = resume9;

      document.getElementById("cible-publication").style.display = "none";
      document.getElementById("cible-format").style.display = "block";
      focusSurSectionSuivante("cible-format");
    }
  }

  // QUESTION 10: Format/Mise en page (collecte d'info uniquement)
  if (cible === "format") {
    if (reponse) {
      const radios = document.getElementsByName('format');
      let resume10 = "10 - Votre document sera : ";

      let optionChoisie10 = "";
      for (let radio of radios) {
        if (radio.checked) {
          optionChoisie10 = radio.value;
          break;
        }
      }
      resume10 += optionChoisie10;
      // Afficher le résultat final
      resultat.style.display = "block";
      document.getElementById('resume10').textContent = resume10;
      document.getElementById("cible-format").style.display = "none";
    }
  }
}

// Réinitialisation du formulaire
document.getElementById("btnReset").addEventListener("click", () => {
  document.getElementById("formCibles").reset();
  document.getElementById("resultat").textContent = ""; // Effacer le résultat
  // Masquer toutes les cibles
  document.querySelectorAll("[id^='cible-']").forEach((section) => {
    section.style.display = "none";
    document.getElementById("cible-organisme").style.display = "block";
    document.getElementById("resume").textContent = "";
    document.getElementById("resume2").textContent = "";
    document.getElementById("resume3").textContent = "";
    document.getElementById("resume4").textContent = "";
    document.getElementById("resume5").textContent = "";
    document.getElementById("resume6").textContent = "";
    document.getElementById("resume7").textContent = "";
    document.getElementById("resume8").textContent = "";
    document.getElementById("resume9").textContent = "";
    document.getElementById("resume10").textContent = "";
  });
});
