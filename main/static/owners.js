// onclick handler function for deleting owners on the owners page
async function deleteOwner(ownerId) {

    // If user confirms, send fetch request to delete endpoint
    const question = 'Are you sure you want to delete this owner?'
    if (window.confirm(question)) {

        // DELETE request is fetched with ownerId
        return await fetch(window.location.href + '/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ owner_id: ownerId })
        }) // user is redirected to refresh/update owners page
        .then((res) => location.reload())
        .catch(err => console.log(err))
    }
}
