// This file is intentionally blank
// Use this file to add JavaScript to your project



function showMenu() {
    
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const hambugerLines = document.getElementById("hamburger-line");

    if (hamburgerMenu.style.display == "none" || hamburgerMenu.style.display == "") {
        hamburgerMenu.style.display = "block";
        hambugerLines.className = "hamburger__line rotate";
    } else {
        hamburgerMenu.style.display = "none";
        hambugerLines.className = "hamburger__line";
    }
}

function showInnerMenu() {
    const dropdownHamburger = document.getElementById("dropdown-hamburger");
    if(dropdownHamburger.style.display == "none" || dropdownHamburger.style.display == "") {
        dropdownHamburger.style.display = "block";
    } else {
        dropdownHamburger.style.display = "none";
    }
}
