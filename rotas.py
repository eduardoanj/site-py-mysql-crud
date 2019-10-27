from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('first_tela.html')

@app.route('/index')
def index():
    return render_template ('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')



app.run()