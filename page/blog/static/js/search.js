document.addEventListener("DOMContentLoaded", function () {
  var searchInput = document.querySelector(".search-input");
  var searchIcon = document.querySelector(".img-search-icon");

  searchInput.addEventListener("input", function () {
    if (searchInput.value.trim() !== "") {
      searchIcon.style.opacity = "0";
    } else {
      searchIcon.style.opacity = "1";
    }
  });
});
