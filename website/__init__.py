from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'v&h0Unm?Hm6zHct*e1=M[tn&7Vw;F=nXraM]Up)+cXrv!\'7t|-6NIeLbmZhE=QAR'
    return app