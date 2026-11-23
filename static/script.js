function destacar(botao) {
    navigation_links[botao].style.backgroundColor="white";
    navigation_links[botao].style.color="purple";
}

function getId(botao) {
    return Number(botao[botao.length]);
}

async function carregarPersonagem(id) {
    const resposta = await fetch(`/${id}`);

    if (!resposta.ok) {
        console.log("Erro ao buscar personagem.");
        return;
    }

    const dados = await resposta.json();

    renderizarPersonagem(dados);
}

const caminho = window.location.pathname;
const baseNavigation = document.getElementById("navigation");
const indexNavigation = document.getElementById("nav-home");

let indexNavigation_links = new Array();

for (let i = 0; i < 6; i++) {
    indexNavigation_links.push(document.getElementById(`nav-${i + 1}`));
}

let navigation_links = new Array();
const enderecos = [
    "/personagem/1", 
    "/personagem/2", 
    "/personagem/3", 
    "/personagem/4", 
    "/personagem/5", 
    "/personagem/6"
];

for (let i = 1; i < 8; i++) {
    navigation_links.push(document.getElementById(`link${i}`));
}

for (let i = 0; i < 6; i++) {
    let id = getId(navigation_links[i + 1]);
    navigation_links[i + 1].addEventListener("clikc", carregarPersonagem(id));

    id = getId(indexNavigation_links[i]);
    indexNavigation_links[i].addEventListener("click", carregarPersonagem(id));
}

for (let i = 0; i < 6; i++) {
    if (caminho === enderecos[i]) {
        destacar(i + 1);
    }
}

if (caminho === "/") {
    baseNavigation.style.display="none";
}