from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Halo Flask, lieur euy "

    @app.route('/about')
    def about():
        return "Tentang saya ........"

    return app
#app.run('0.0.0.0', debug=True)