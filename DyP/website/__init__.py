from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRETE_KEY'] = 'lkl;a;a;s;s;dsfsdfdfsdfsdfsdfsdfsdll'
    
    return app