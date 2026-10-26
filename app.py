from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)