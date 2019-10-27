for (let link of document.querySelectorAll('.note-edit-link')){
    link.addEventListener('click', event => {
        link.parentElement.querySelector('.note-body').style.display='none'
        link.parentElement.querySelector('.note-edit-link').style.display='none'
        link.parentElement.querySelector('.note-delete-link').style.display='none'
        link.parentElement.querySelector('.body-edit-form').style.display='inline-block'
        link.parentElement.querySelector('.edit-cancel').style.display='flex'
    })
}

for (let link of document.querySelectorAll('.note-delete-link')){
    link.addEventListener('click', event => {
        link.parentElement.querySelector('.note-delete-link').style.display='none'
        link.parentElement.querySelector('.note-edit-link').style.display='none'
        link.parentElement.querySelector('.delete-note-form').style.display='inline-block'
    })
}

// for (let link of document.querySelectorAll('.comment-button')){
//     link.addEventListener('click', event => {
//         link.parentElement.querySelector('.comment-link').style.display='none'
//         link.parentElement.querySelector('.comment-form').style.display='inline-block'
//     })
// }
