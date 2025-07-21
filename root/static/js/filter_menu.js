document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".filters_menu li");
  const productItems = document.querySelectorAll(".filters-content .col-sm-6");

  filterButtons.forEach(button => {
    button.addEventListener("click", function () {
      const selected = this.getAttribute("data-filter");

      // Убираем класс active у всех и ставим текущему
      filterButtons.forEach(btn => btn.classList.remove("active"));
      this.classList.add("active");

      productItems.forEach(item => {
        if (selected === "all") {
          item.style.display = "block";
        } else {
          // Сравниваем data-filter с классом (например "burger", "pizza")
          if (item.classList.contains(selected)) {
            item.style.display = "block";
          } else {
            item.style.display = "none";
          }
        }
      });
    });
  });
});
