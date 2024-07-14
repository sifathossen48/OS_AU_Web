//FAQ

const items = document.querySelectorAll('.accordion button');

function toggleAccordion() {
    const itemToggle = this.getAttribute('aria-expanded');

    for (i = 0; i < items.length; i++) {
        items[i].setAttribute('aria-expanded', 'false');
    }

    if (itemToggle == 'false') {
        this.setAttribute('aria-expanded', 'true');
    }
}

items.forEach((item) => item.addEventListener('click', toggleAccordion));

const txts = document.querySelector(".animate-text").children,
    txtsLen = txts.length;
let index = 0;
const textInTimer = 3000,
    textOutTimer = 2800;

function animateText() {
    for (let i = 0; i < txtsLen; i++) {
        txts[i].classList.remove("text-in", "text-out");
    }
    txts[index].classList.add("text-in");

    setTimeout(function () {
        txts[index].classList.add("text-out");
    }, textOutTimer)

    setTimeout(function () {

        if (index == txtsLen - 1) {
            index = 0;
        }
        else {
            index++;
        }
        animateText();
    }, textInTimer);
}
window.onload = animateText;

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    responsiveClass: true,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,
    responsive: {
        0: {
            items: 1,
            nav: false
        },
        600: {
            items: 4,
            nav: false
        },
        1000: {
            items: 7,
            nav: false,
        }
    }
});