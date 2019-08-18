import 'materialize-css/dist/css/materialize.css';
import 'materialize-css/dist/js/materialize.js';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './fonts/fonts.css';
import './style.scss';
import './style/content.scss';
console.log("[EMIT] Ready");

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.parallax');
  var instances = M.Parallax.init(elems);
});


// function resizeGroups()
// {
//   clientHeight
// document.querySelector('.art-group').clientHeight
// }

