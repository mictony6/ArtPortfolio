var slides = document.getElementsByClassName("slide");
var counter = document.getElementById("counter");
var dots;
let currentSlide = 0;
let navigation = document.querySelectorAll(".nav ul li");

let summary_text = document.querySelector(".summary p");


initialize();
resize_to_fit();

dots = document.getElementsByClassName("dot");
slideShow();



function initialize() {
    let n = slides.length;
    for (let i = 0; i < n; i++) {
        counter.appendChild(newDot());
    }
    console.log(summary_text);

}

function resize_to_fit() {
    let fontSize = window.getComputedStyle(summary_text).fontSize;


    if ((summary_text.clientHeight + summary_text.previousElementSibling.clientHeight) >= summary_text.parentNode.clientHeight) {
        summary_text.style.fontSize = (parseFloat(fontSize) - 1) + 'px';
        console.log(summary_text.clientHeight + summary_text.previousElementSibling.clientHeight - summary_text.parentNode.clientHeight);
        resize_to_fit();

    }

}


function newDot() {

    let dot = document.createElement("div");
    dot.className = "dot";
    return dot;
}


function slideShow() {
    let n = slides.length;
    for (let i = 0; i < n; i++) {
        slides[i].style.display = "none";
        dots[i].style = "background-color:var(--accent)";

    }
    slides[currentSlide].style.display = "flex";
    dots[currentSlide].style = "background-color:var(--powder)";

    currentSlide++;
    currentSlide %= n;
    setTimeout(slideShow, 5000);
}







