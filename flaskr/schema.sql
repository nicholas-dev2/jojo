
CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    resumo TEXT NOT NULL,
    imagem TEXT,
    descricao_imagem TEXT
);

CREATE TABLE IF NOT EXISTS secoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    personagem_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT,
    tipo_lista TEXT NOT NULL DEFAULT 'ul'
        CHECK (tipo_lista IN ('ul', 'ol')),

    FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS habilidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    secao_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,

    FOREIGN KEY (secao_id)
        REFERENCES secoes(id)
        ON DELETE CASCADE
);
