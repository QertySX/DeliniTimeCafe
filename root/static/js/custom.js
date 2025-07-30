function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    var displayYearElement = document.querySelector("#displayYear");
    if (displayYearElement) {
        displayYearElement.innerHTML = currentYear;
    }
}

$(document).ready(function() {
    getYear();

    var $grid; 
    $(window).on('load', function () {
        $('.filters_menu li').click(function () {
            $('.filters_menu li').removeClass('active');
            $(this).addClass('active');

            var data = $(this).attr('data-filter');
            if ($grid) {
                $grid.isotope({
                    filter: data
                });
            }
        });

        $grid = $(".grid").isotope({
            itemSelector: ".all",
            percentPosition: false,
            masonry: {
                columnWidth: ".all"
            }
        });
    });

    // nice select
    $('select').niceSelect();

    // client section owl carousel
    $(".client_owl-carousel").owlCarousel({
        loop: true,
        margin: 0,
        dots: false,
        nav: true,
        navText: [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        autoplay: true,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });

    function myMap() {
        var mapProp = {
            center: new google.maps.LatLng(40.712775, -74.005973),
            zoom: 18,
        };
        var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    }
    if ($("#googleMap").length) {
        myMap();
    }
});