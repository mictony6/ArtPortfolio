let items = document.querySelectorAll('.item')
let gallery = document.querySelector(".gallery");
let dimPanel = document.createElement("div");
dimPanel.className = "dim-panel";






items.forEach((item) => {
    item.onmouseover = () => {
        item.appendChild(dimPanel);
        dimPanel.style.position = 'absolute';
        showDimPanel(item.firstElementChild.getAttribute('data-likes'))

        console.log();

    }
    item.onmouseleave = () => {
        dimPanel.style.display = "none";
        item.removeChild(dimPanel);

    }

});

function showDimPanel(n) {
    dimPanel.style.display = "block";
    dimPanel.innerHTML = n + " likes";
}


