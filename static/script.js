const caminho = window.location.pathname;
const navigation = document.getElementById("navigation");

if (caminho === "/") {
    navigation.style.visibility="hidden";
}