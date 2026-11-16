function destacar(botao) {
    navigation_links[botao].style.backgroundColor="white";
    navigation_links[botao].style.color="purple";
}

const caminho = window.location.pathname;
const navigation = document.getElementById("navigation");

let navigation_links = new Array();
const enderecos = ["/jonathan", "/joseph", "/jotaro", "/josuke", "/giorno", "/jolyne"];

for (let i = 1; i < 8; i++) {
    navigation_links.push(document.getElementById(`link${i}`));
}

for (let i = 0; i < 6; i++) {
    if (caminho === enderecos[i]) {
        destacar(i + 1);
    }
}

if (caminho === "/") {
    navigation.style.display="none";
}