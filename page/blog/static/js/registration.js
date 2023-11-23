const formField = document.querySelector('.registration-container');

if (formField) {
    setTimeout(() => {
        formField.scrollIntoView({
            behavior: 'smooth',
            block: 'center',
            inline: 'nearest'
        });
    }, 1000);
}
