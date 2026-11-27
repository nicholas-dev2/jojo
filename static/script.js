async function searchData(nome) {
    const resposta = await fetch(`/api/${nome}`);
    const dados = await resposta.json();
    return dados;
}

function destacar(indice) {
    baseNavigation[indice].style.backgroundColor='white';
    baseNavigation[indice].style.color='purple';
}

function fillData(dados) {
    nome.textContent = dados.nome;
    imagem.src=`/static/imagens/${dados.imagem}`;
    resumo.textContent = dados.resumo;
    tituloSecao.textContent = dados.secoes[0].titulo;
    descricacaoSecao.textContent = dados.secoes[0].descricao;
    habilidade1.textContent = dados.secoes[0].habilidades[0].titulo + ": " + dados.secoes[0].habilidades[0].descricao;
    habilidade2.textContent = dados.secoes[0].habilidades[1].titulo + ": " + dados.secoes[0].habilidades[1].descricao;
    habilidade3.textContent = dados.secoes[0].habilidades[2].titulo + ": " + dados.secoes[0].habilidades[2].descricao;
    habilidade4.textContent = dados.secoes[0].habilidades[3].titulo + ": " + dados.secoes[0].habilidades[3].descricao;
}

function registerButtons(inicio, fim, lista, radical) {
    for (let i = inicio; i < fim; i++) {
        let botao = document.getElementById(`${radical}${i}`);
        lista.push(botao);
    }
}

function editar(protagonista) {
    painelEdicao.style.display = "block";
}

const caminho = window.location.pathname
const indexNavigation = new Array();
const baseNavigation = new Array();
const navigation = document.getElementById("navigation");

let painelEdicao = document.getElementById("painel");
let nome = document.getElementById("nome");
let imagem = document.getElementById("imagem");
let resumo = document.getElementById("resumo");
let tituloSecao = document.getElementById("tituloSecao");
let descricacaoSecao = document.getElementById("descricaoSecao");
let habilidade1 = document.getElementById("habilidade1");
let habilidade2 = document.getElementById("habilidade2");
let habilidade3 = document.getElementById("habilidade3");
let habilidade4 = document.getElementById("habilidade4");

const protagonistas = [
    "jonathan",
    "joseph",
    "jotaro",
    "josuke",
    "giorno",
    "jolyne"
];

registerButtons(2, 8, baseNavigation, "link");

if (caminho === "/") {
    registerButtons(1, 7, indexNavigation, "nav-");
    navigation.style.display='none';
} else if (caminho != "/" && caminho != "/editor") {
    destacar(protagonistas.indexOf(caminho.slice(1)));
}


for (let i = 0; i < 6; i++) {
    if (caminho === "/") {
        indexNavigation[i].addEventListener("click", () => searchData(protagonistas[i]));
    } else if (caminho != "/editor") {
        baseNavigation[i].addEventListener("click", () => searchData(protagonistas[i]));
    }
}

if (protagonistas.includes(caminho.slice(1))) {
    searchData(caminho.slice(1)).then(dados => {
        fillData(dados);
    });
}

if (caminho === "/editor") {
    const editores = new Array();

    for (let i = 0; i < 6; i++) {
        editores.push(document.getElementById(`editar${i + 1}`));
    }

    for (let i = 0; i < 6; i++) {
        editores[i].addEventListener("click", () => editar(protagonistas[i]));
    }
}