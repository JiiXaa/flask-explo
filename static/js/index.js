/**
 * Add active class to the current button (highlight it) when the page is loaded or refreshed
 */

// !! need to figure out how to add active class to link when page is refreshed or loaded !!
// navigationLinks.forEach((link) => {
//   link.addEventListener('click', (e) => {
//     e.preventDefault();
//     navigationLinks.forEach((link) => {
//       link.classList.remove('active');
//     });
//     link.classList.add('active');
//   });
// });

const currentLocation = location.href;
const navigationLinks = document.querySelectorAll('#nav-link');
const navigationLength = navigationLinks.length;

for (let i = 0; i < navigationLength; i++) {
  if (navigationLinks[i].href === currentLocation) {
    navigationLinks[i].classList.add('active');
  }
}
