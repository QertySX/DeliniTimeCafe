$(document).ready(function () {
  const $products = $(".filters-content .row .col-sm-6, .filters-content .row .col-lg-4");
  const $btn = $("#view-more-btn");
  let visibleCount = 3;

  function showProducts() {
    $products.each(function (index) {
      if (index < visibleCount) {
        $(this).show();
      } else {
        $(this).hide();
      }
    });

    if (visibleCount >= $products.length) {
      $btn.hide();
    }
  }

  showProducts();

  $btn.on("click", function (e) {
    e.preventDefault();
    visibleCount += 3;
    showProducts();
  });
});

