$(document).ready(function () {
    $('.toggle').click(function () {
        $('.toggle').toggleClass('active')
        $('nav ul').toggleClass('active-menu')
    })
})

const section = document.querySelectorAll('section');
const navA = document.querySelectorAll('nav ul li a');
console.log(navA);
window.addEventListener('scroll', ()=> {
    let current = '';

    section.forEach( section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - sectionHeight / 3)) {
            current = section.getAttribute('id');
        }
    })

    navA.forEach( a => {
        a.classList.remove('active');
        if(a.classList.contains(current)) {
            a.classList.add('active')
        }
    })
    //console.log(current);
})