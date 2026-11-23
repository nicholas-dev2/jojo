from flask import Flask, render_template, jsonify
import os
from flaskr.database import get_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/personagem/<int:id_protagonista>')
    def personagem(id_protagonista):
        return render_template(
            'personagem.html',
            personagem_id=id_protagonista
        )

    @app.route('/<int:id_protagonista>')
    def buscar_personagem(id_protagonista):
        db = get_db()

        protagonista = db.execute('SELECT * FROM personagens WHERE id = ?', 
            (id_protagonista,)).fetchone()
        
        if protagonista is None:
            return jsonify({'erro': 'Personagem não encontrado'}), 404
        
        secoes = db.execute(
            'SELECT * FROM secoes WHERE personagem_id = ?',
        (id_protagonista,)).fetchall()

        resultado = dict(protagonista)
        resultado['secoes'] = []

        for secao in secoes:
            habilidades = db.execute(
                'SELECT * FROM habilidades WHERE secao_id = ?',
                (secao['id'],)
            ).fetchall()

            secao_dict = dict(secao)
            secao_dict['habilidades'] = [
                dict(habilidade) for habilidade in habilidades
            ]

            resultado['secoes'].append(secao_dict)

        return jsonify(resultado)

    @app.route('/editor')
    def editor():
        return render_template('admin/editor.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)