function initClickEvent(){$(document).one("click",function(e){var menu = $("#mainMenu");var menuBtn = document.getElementById("menuIcon");if(!menu.is(e.target) && menu.has(e.target).length === 0 &&!$(menuBtn).is(e.target)){closeMenu(menuBtn)}else{initClickEvent()}})}function openOverlay(overlay){overlay.setAttribute("status","open");return}function closeOverlay(overlay){overlay.setAttribute("status","closed");return}function toggleOverlay(){var overlay = document.getElementById("overlay");var status = overlay.getAttribute("status");switch(status){case "open":closeOverlay(overlay);break;case "closed":openOverlay(overlay);break;default:closeOverlay(overlay)}return}