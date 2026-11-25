import json
from .database import get_db
import click
from flask.cli import with_appcontext

protagonistas = [
    'jonathan',
    'joseph',
    'jotaro',
    'josuke',
    'giorno',
    'jolyne'
]

def fill_db():
    db = get_db()

    with db:
        for protagonista in protagonistas:
            with open(f'data/{protagonista}.json', 'r', encoding='utf8') as dados:
                personagem = json.load(dados)

                db.execute('''
                    INSERT INTO personagens(
                        nome, resumo, imagem, descricao_imagem, slug
                    )

                    VALUES (?, ?, ?, ?, ?)

                    ON CONFLICT(nome) DO UPDATE SET
                        resumo = excluded.resumo,
                        imagem = excluded.imagem,
                        descricao_imagem = excluded.descricao_imagem,
                        slug = excluded.slug
                ''', (

                    personagem['nome'],
                    personagem['resumo'],
                    personagem['imagem'],
                    personagem.get('descricao_imagem'),
                    protagonista
                ))

                id_protagonista = db.execute(
                    'SELECT id FROM personagens WHERE nome = ?',
                    (personagem['nome'],)
                ).fetchone()['id']

                db.execute(
                    'DELETE FROM secoes WHERE personagem_id = ?',
                    (id_protagonista,)
                )

                for seção in personagem['secoes']:
                    cursor = db.execute('''
                        INSERT INTO secoes
                            (personagem_id, titulo, descricao, tipo_lista)
                        VALUES (?, ?, ?, ?)
                    ''', (
                        id_protagonista,
                        seção['titulo'],
                        seção['descricao'],
                        seção.get('tipo_lista', 'ul')
                    ))

                    id_seção = cursor.lastrowid

                    for habilidade in seção['habilidades']:
                        db.execute('''
                            INSERT INTO habilidades
                                (secao_id, titulo, descricao)
                            VALUES (?, ?, ?)
                        ''', (
                            id_seção,
                            habilidade['titulo'],
                            habilidade['descricao']
                        ))

@click.command('fill-db')
@with_appcontext
def fill_db_command():
    fill_db()
    click.echo('Banco de dados preenchido!')