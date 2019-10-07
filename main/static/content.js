// Prompts users for confirmation when deleting owners
if (window.location.pathname === '/owners') {
    // Obtains all trash icon elements
    const allTrash = document.querySelectorAll('.trash')

    // For each trash icon, add an eventlistener that triggers prompt upon click
    allTrash.forEach(e => {
        e.addEventListener('click', () => {
            const question = 'Are you sure you want to delete this owner?'
            // If user confirms, send request to delete endpoint
            if (window.confirm(question)) {
                const id = e.parentElement.parentElement.children[0].innerHTML
                window.location.pathname = `owners/delete/${id}`
            }
        })
    });
}
