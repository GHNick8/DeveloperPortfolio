// Show button when user scrolls down 300px
window.onscroll = function() { scrollFunction(); };

function scrollFunction() {
    let scrollBtn = document.getElementById("scrollBtn");
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        scrollBtn.style.display = "block";
    } else {
        scrollBtn.style.display = "none";
    }
}

// Scroll to the top smoothly
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}