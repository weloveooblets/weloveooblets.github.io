import 'materialize-css/dist/css/materialize.css';
import 'materialize-css/dist/js/materialize.js';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './style.scss';
console.log("[EMIT] Ready");

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.parallax');
  var instances = M.Parallax.init(elems);
});