document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Зупинити стандартну відправку форми

        // Отримати значення полів форми
        const username = document.getElementById("id_username").value;
        const password = document.getElementById("id_password").value;

        // Ваша логіка обробки даних або відправлення на сервер
        // Наприклад, ви можете використовувати fetch або відправити AJAX запит
        // Замість цього місця буде ваша власна обробка даних або відправка на сервер
        console.log("Username:", username);
        console.log("Password:", password);

        // Очистити значення полів після відправки форми
        document.getElementById("id_username").value = "";
        document.getElementById("id_password").value = "";
    });
});
