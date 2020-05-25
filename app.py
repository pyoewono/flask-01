from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Halo Flask"

@app.route('/about')
def about():
    return "Tentang saya"

app.run('0.0.0.0', debug=True)