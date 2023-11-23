// (() => {
//   const menuBtnRef = document.querySelector("[data-menu-button]");
//   const mobileMenuRef = document.querySelector("[data-menu]");
//   menuBtnRef.addEventListener("click", () => {
//     const expanded =
//       menuBtnRef.getAttribute("aria-expanded") === "true" || false;
//     menuBtnRef.classList.toggle("is-open");
//     menuBtnRef.setAttribute("aria-expanded", !expanded);
//     mobileMenuRef.classList.toggle("is-open");
//   });
// })();

// (() => {
//   const menuBtnRef = document.querySelector("[data-menu-button]");
//   const mobileMenuRef = document.querySelector("[data-menu]");
//   const userActionsRef = document.querySelector(".user-actions"); // Знаходимо елемент .user-actions

//   menuBtnRef.addEventListener("click", () => {
//     const expanded =
//       menuBtnRef.getAttribute("aria-expanded") === "true" || false;
//     menuBtnRef.classList.toggle("is-open");
//     menuBtnRef.setAttribute("aria-expanded", !expanded);
//     mobileMenuRef.classList.toggle("is-open");

//     // Додаємо/видаляємо клас is-open для .user-actions
//     userActionsRef.classList.toggle("is-open");
//   });
// })();
(() => {
  const menuBtnRef = document.querySelector("[data-menu-button]");
  const mobileMenuRef = document.querySelector("[data-menu]");
  const hiddenActionsRef = document.querySelector(".is-hidden");
  const userActionsRef = document.querySelector(".user-actions");

  menuBtnRef.addEventListener("click", () => {
    const expanded = menuBtnRef.getAttribute("aria-expanded") === "true" || false;
    menuBtnRef.classList.toggle("is-open");
    menuBtnRef.setAttribute("aria-expanded", !expanded);
    mobileMenuRef.classList.toggle("is-open");

    if (mobileMenuRef.classList.contains("is-open")) {
      hiddenActionsRef.classList.remove("is-hidden");
      hiddenActionsRef.classList.add("user-actions", "is-open"); // Додаємо класи user-actions та is-open
      userActionsRef.classList.add("is-hidden");
    } else {
      hiddenActionsRef.classList.add("is-hidden");
      hiddenActionsRef.classList.remove("user-actions", "is-open"); // Видаляємо класи user-actions та is-open
      userActionsRef.classList.remove("is-hidden");
    }
  });
})();
