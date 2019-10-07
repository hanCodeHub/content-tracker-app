// Switches active state between navs when new page loads

// First remove the current active class
const currentActive = document.querySelector('.active')
currentActive.classList.remove('active')

// Obtain current page from the URL
const currentPageName = window.location.pathname.substring(1)

// Find the link that matches the current page name and add active class
const navLinks = document.querySelectorAll('.nav-link')
navLinks.forEach((link) => {
    if (link.innerHTML.toLowerCase() === currentPageName.toLowerCase()) {
        link.parentElement.classList.add('active')
    }
})
