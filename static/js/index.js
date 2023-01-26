const navigationLinks = document.querySelectorAll('#nav-link');

/**
 * Add active class to the current button (highlight it)
 */

// !! need to figure out how to add active class to link when page is refreshed or loaded !!
navigationLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    navigationLinks.forEach((link) => {
      link.classList.remove('active');
    });
    link.classList.add('active');
  });
});
