document.addEventListener("DOMContentLoaded", function () {
  const image = document.querySelector(".lightbox-image");
  const modal = document.querySelector(".lightbox");

  const galleryImages = document.querySelectorAll(".gallery");

  galleryImages.forEach((img) => {
    img.addEventListener("click", () => {
      image.src = img.dataset.source;
      image.alt = img.alt;
      modal.classList.add("is-open");
    });
  });

  modal.addEventListener("click", (event) => {
    if (
      event.target === modal ||
      event.target.classList.contains("lightbox-button")
    ) {
      modal.classList.remove("is-open");
    }
  });
});
