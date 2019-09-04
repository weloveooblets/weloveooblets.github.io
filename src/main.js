import 'materialize-css/dist/css/materialize.css';
import 'materialize-css/dist/js/materialize.js';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './fonts/fonts.css';
import './style.scss';
import './style/content.scss';

console.log("[EMIT] Ready");

document.addEventListener('DOMContentLoaded', function () {
  addParallax();
  addReveal();

  document.querySelector('#top').addEventListener('click', backToTop);
});

function addParallax() {
  let els = document.querySelectorAll('.parallax');
  let instances = M.Parallax.init(els, { responsiveThreshold: 0 });
}

function backToTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function addReveal() {
  // let els = document.querySelectorAll('.tt');
  // let instances = M.Tooltip.init(els, {
  //   margin: 0,
  //   position: 'bottom',
  //   transitionMovement: 0,
  // });

  //console.log(ttInstances);

  /* function onReveal(el) {
    let instance = M.Tooltip.getInstance(el);
    if (instance) {
      // instance.open();
      // instance.close();
      let delay = Math.random() * 200 + 100;
      let duration = 1000;
      setTimeout(() => { instance.open() }, delay);
      setTimeout(() => { instance.close() }, delay + duration);
    }
  } */


  let viewFactor = 0;
  let reset = false;

  // ScrollReveal().reveal(els, { afterReveal: onReveal, viewFactor: viewFactor });
  // ScrollReveal().reveal(document.querySelectorAll('.quote-wrapper'), { viewFactor: viewFactor });
  ScrollReveal.debug = true;
  ScrollReveal().reveal(document.querySelectorAll('.art-wrapper, .quote-wrapper'),
    {
      viewFactor: viewFactor,
      reset: reset,
      viewOffset: {
        top: 0,
        right: -200,
        bottom: 0,
        left: -200,
      }
    });

}