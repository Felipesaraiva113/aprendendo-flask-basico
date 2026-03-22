from flask import Flask
from blueprints.mensagens.mensagens import mensagens_bp
from blueprints.calculadora.calculadora import calculadora_bp
app = Flask(__name__)
app.register_blueprint(mensagens_bp,url_prefix='/mensagens')
app.register_blueprint(calculadora_bp,url_prefix='/calculadora')
@app.route('/')
def index():
    return 'olá!'
if __name__ == '__main__':
    app.run(debug=True)