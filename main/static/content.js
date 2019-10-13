// onclick handler function for editing content on the content page
function editContent(contentId) {
    location.pathname = `/content/edit/${contentId}`
}

// onclick handler function for deleting content on the content page
async function deleteContent(contentId) {

    // If user confirms, send fetch request to delete endpoint
    const question = 'Are you sure you want to delete this content?'
    if (window.confirm(question)) {

        // DELETE request is fetched with contentId
        return await fetch(window.location.href + '/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content_id: contentId })
        }) // user is redirected to refresh/update content page
            .then((res) => location.reload())
            .catch(err => console.log(err))
    }
}