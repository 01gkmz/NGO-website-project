(function($) {
    'use strict';
    //¸ü¶àÏÂÔØ£ºhttp://www.bootstrapmb.com
    // Header Search
    if ($('.btn-search').length) {
        $('.btn-search').on('click', function(event) {
            $('body').addClass('search-active');
            event.preventDefault();
        });
        $('.close-search').on('click', function() {
            $('body').removeClass('search-active');
        });
        
    }

    // Hero Video
    //$(".play-3").yu2fvl({ vid: "ZG6tNrxXh1k", ratio: 4/3 });


    // Counter
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    //  Testimonial
    $('.customer-slider').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        nav: true,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1,
                nav: false,
            },
            600: {
                items: 1,
                nav: false,
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1000: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })

    //  Testimonial Home 2
    $('.testimonial-slider-v2').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        autoHeight:true,
        nav: true,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1,
                nav: false,
            },
            600: {
                items: 1,
                nav: false,
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1000: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })


    //  Blog Slider
    $('.blog-bottom-slide').owlCarousel({
        loop: true,
        autoplay: true,
        margin: 30,
        smartSpeed: 1500,
        dots: false,
        nav: false,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1,
                nav: false,
            },
            600: {
                items: 2
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1000: {
                items: 2
            },
            1920: {
                items: 2
            }
        }
    })

    // Hamburger Menu
    $('.sub-btn').click(function(event){
        $(this).next('.submenu').slideToggle();
        event.preventDefault();
    });
    $('.hamburger-menu').click(function() {
        $('.header-menu').addClass('active');
    });
    $('.close-btn').click(function() {
        $('.header-menu').removeClass('active');
    });

    // sticky Header
    var wind = $(window);
    var sticky = $('#sticky-header');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });


    //  About US Home 3
    $('.about-v3-slide').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        autoHeight:true,
        nav: false,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1,
                nav: false,
            },
            600: {
                items: 1,
                nav: false,
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1000: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })

    //  Testimonial Home 3
    $('.feedback-v3-slide').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        autoHeight:true,
        nav: true,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1,
                nav: false,
            },
            600: {
                items: 1,
                nav: false,
            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1000: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })

    //  Blog Slider Home 3
    $('.blog-bottom-slide-v3').owlCarousel({
        loop: true,
        autoplay: true,
        margin: 30,
        smartSpeed: 1500,
        dots: false,
        nav: false,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1,
                nav: false,
            },
            600: {
                items: 2,
                margin: 30
            },
            768: {
                items: 2,
                margin: 30
            },
            992: {
                items: 3,
                margin: 30
            },
            1000: {
                items: 3,
                margin: 30
            },
            1920: {
                items: 3,
                margin: 30
            }
        }
    })

    // WOW JS
    new WOW().init();
    
   

   $(window).on('load', function () {
        // Window Loading JS
        $(".lds-ripple").fadeOut();
        $(".nexigen-loading").delay(450).fadeOut('slow');
   });

})(jQuery);
