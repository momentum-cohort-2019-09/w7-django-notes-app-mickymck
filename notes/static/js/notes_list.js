for (let link of document.querySelectorAll('.note-edit-link')){
    link.addEventListener('click', event => {
        link.parentElement.querySelector('.note-body').style.display='none'
        link.parentElement.querySelector('.body-edit-form').style.display='inline-block'
    })
}
