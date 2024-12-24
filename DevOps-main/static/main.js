'use strict';

function openLink(event) {
    let row = event.target.closest('.row');
    if (row.dataset.url) {
        window.location = row.dataset.url;
    }
}


const TOOLBAR_ITEMS = [
    "bold", "italic", "heading", "|", 
    "quote", "ordered-list", "unordered-list", "|",
    "link", "upload-image", "|",  
    "preview", "side-by-side", "fullscreen", "|",
    "guide"
]

window.onload = function() {
    var myModalEl = document.getElementById('delete-book-modal')
    myModalEl.addEventListener('show.bs.modal', function (event) {
        let form = this.querySelector('form');
        form.action = event.relatedTarget.dataset.url;
        let userNameEl = document.getElementById('book-title');
        userNameEl.innerHTML = event.relatedTarget.closest('th').querySelector('.book-title').textContent;
})
    let background_img_field = document.getElementById('cover_img');
    if (background_img_field) {
        background_img_field.onchange = imagePreviewHandler;
    }
    for (let course_elm of document.querySelectorAll('.courses-list .row')) {
        course_elm.onclick = openLink;
    }
    if (document.getElementById('text-content')) {
        let easyMDE = new EasyMDE({
            element: document.getElementById('text-content'),
            toolbar: TOOLBAR_ITEMS,
            uploadImage: true,
            imageUploadEndpoint: '/api/images/upload',
            imageUploadFunction: imageUploadFunction
        });
    }
}