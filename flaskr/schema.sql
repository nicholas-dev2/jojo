CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    resumo TEXT NOT NULL,
    imagem TEXT,
    tipo_lista TEXT NOT NULL DEFAULT 'ul'
        CHECK (tipo_lista IN ('ul', 'ol'))
)

CREATE TABLE IF NOT EXISTS habilidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    personagem_id INTEGER NOT NULL,
    titulo_seção TEXT NOT NULL,
    descrição_seção TEXT NOT NULL,
    item1 TEXT NOT NULL,
    item2 TEXT NOT NULL,
    item3 TEXT NOT NULL,
    
    FOREIGN KEY (personagem_id)
        REFERENCES personagens(id)
        ON DELETE CASCADE
)