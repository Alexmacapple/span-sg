document.addEventListener("DOMContentLoaded", addBackToTopButton);
document.addEventListener("DOMContentLoaded", checkboxReplacer);
document.addEventListener("DOMContentLoaded", strikethroughReplacer);
document.addEventListener("DOMContentLoaded", copyCode);

function addBackToTopButton() {
  console.log("Check if add back to top is needed");
  if (document.documentElement.scrollHeight > window.innerHeight * 2) {
    console.log("Back to top is needed");
    const link = document.createElement("a");
    link.className = "fr-link fr-icon-arrow-up-fill fr-link--icon-left";
    link.href = "#top";
    link.textContent = "Haut de page";

    const contenuDiv = document.getElementById("backtop");
    if (contenuDiv) {
      contenuDiv.appendChild(link);
    }
  } else {
    console.log("Back to top is not needed");
  }
}

function copyCode() {
  const codeBlocks = document.querySelectorAll("pre > code");
  console.log(codeBlocks);

  codeBlocks.forEach((codeBlock, index) => {
    const copyButton = document.createElement("button");
    copyButton.textContent = "Copier";
    copyButton.className = "fr-btn fr-btn--sm copy-code-button fr-btn--secondary";
    copyButton.setAttribute("data-clipboard-index", index);
    codeBlock.parentElement.style.position = "relative";
    codeBlock.parentElement.appendChild(copyButton);

    copyButton.addEventListener("click", (event) => {
      const textarea = document.createElement("textarea");
      textarea.textContent = codeBlock.textContent;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);

      // Indiquer que le texte a été copié
      copyButton.textContent = "Copié !";
      setTimeout(() => {
        copyButton.textContent = "Copier";
      }, 2000);
    });
  });
}

function checkboxReplacer() {
  // Sélectionner tous les éléments avec la classe 'markdown-content'
  const markdownElements = document.querySelectorAll(".markdown-content");

  // Parcourir chaque élément ayant la classe 'markdown-content'
  markdownElements.forEach((element) => {
    // Obtenir tous les éléments de liste dans chaque élément 'markdown-content'
    const listItems = element.querySelectorAll("li");

    // Parcourir chaque élément de la liste
    listItems.forEach((listItem) => {
      let innerHTML = listItem.innerHTML;

      // Remplacer [x] par une case à cocher cochée en HTML ou [ ] par une case non cochée
      if (innerHTML.includes("[x]") || innerHTML.includes("[ ]")) {
        // Supprimer les balises <p> enveloppantes si elles existent
        innerHTML = innerHTML.replace(/<p>(.*?)<\/p>/g, "$1").trim();

        // Appliquer des styles en ligne pour supprimer le style de liste
        listItem.style.listStyleType = "none";

        // Si la tâche est cochée ([x])
        if (innerHTML.includes("[x]")) {
          const taskDescription = innerHTML.replace("[x]", "").trim();
          listItem.innerHTML = `
                  <div class="fr-checkbox-group">
                      <input  id="checkbox-${taskDescription}" type="checkbox" checked>
                      <label class="fr-label" for="checkbox-${taskDescription}">
                          ${taskDescription}
                      </label>
                  </div>`;
        }

        // Si la tâche n'est pas cochée ([ ])
        else if (innerHTML.includes("[ ]")) {
          const taskDescription = innerHTML.replace("[ ]", "").trim();
          listItem.innerHTML = `
                  <div class="fr-checkbox-group">
                      <input id="checkbox-${taskDescription}" type="checkbox">
                      <label class="fr-label" for="checkbox-${taskDescription}">
                          ${taskDescription}
                      </label>
                  </div>`;
        }
      }
    });
  });
}

function strikethroughReplacer() {
  // Sélectionne tous les éléments avec la classe markdown-content
  const markdownElements = document.querySelectorAll(".markdown-content");

  markdownElements.forEach((element) => {
    let innerHTML = element.innerHTML;

    // Remplace ~~texte~~ par <del>texte</del>
    innerHTML = innerHTML.replace(/~~(.*?)~~/g, "<del>$1</del>");

    element.innerHTML = innerHTML;
  });
}
