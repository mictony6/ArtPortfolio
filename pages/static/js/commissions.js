const home = document.getElementById("home");
const commissions = document.getElementById("commissions");
const about = document.getElementById("about");


home.onclick = function () {
    this.className = "active";
    commissions.className = "";
    about.className = "";

}

commissions.onclick = function () {
    this.className = "active";
    home.className = "";
    about.className = "";

}
about.onclick = function () {
    this.className = "active";
    commissions.className = "";
    home.className = "";

}

