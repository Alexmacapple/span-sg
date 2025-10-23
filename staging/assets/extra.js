// Force target="_blank" pour liens externes GitHub
document.addEventListener('DOMContentLoaded', function() {
  // Cibler tous les liens vers GitHub dans le header et la nav
  const links = document.querySelectorAll('a[href*="github.com"]');
  links.forEach(function(link) {
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
    link.setAttribute('title', 'Code source GitHub ouvrir dans une nouvelle fenêtre');
  });
});
