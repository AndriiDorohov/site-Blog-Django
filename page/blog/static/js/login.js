const formField = document.querySelector('.form-login-container');

if (formField) {
    setTimeout(() => {
        formField.scrollIntoView({
            behavior: 'smooth',
            block: 'center',
            inline: 'nearest'
        });
    }, 1000);
}
