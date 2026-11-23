from flask import Flask, render_template
import os

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

    @app.route('/jonathan')
    def jonathan():
        return render_template('jonathan.html')

    @app.route('/joseph')
    def joseph():
        return render_template('joseph.html')

    @app.route('/jotaro')
    def jotaro():
        return render_template('jotaro.html')

    @app.route('/josuke')
    def josuke():
        return render_template('josuke.html')

    @app.route('/giorno')
    def giorno():
        return render_template('giorno.html')

    @app.route('/jolyne')
    def jolyne():
        return render_template('jolyne.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)