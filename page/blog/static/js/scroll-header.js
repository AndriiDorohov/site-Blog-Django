window.addEventListener("scroll", function () {
  const yOffset = window.pageYOffset;
  const header = document.querySelector(".page-header");
  header.style.backgroundPositionY = `${yOffset * 0.5}px`;
});
