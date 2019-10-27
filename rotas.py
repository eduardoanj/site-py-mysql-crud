from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicial():
    return ('olaaaaar pessoas')



app.run()