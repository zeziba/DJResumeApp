document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener('scroll', function() {
        let navbar_height = this.document.querySelector('.navbar').offSetHeight;
        if (window.scrollY > 50) {
            this.document.getElementById('navbar-top').classList.add('fixed-top');
            this.document.body.style.paddingTop = navbar_height + 'px';
        } else {
            this.document.getElementById('navbar-top').classList.remove('fixed-top');
            this.document.body.style.paddingTop = navbar_height;
        }
    });
});
// DOMContentLoaded End