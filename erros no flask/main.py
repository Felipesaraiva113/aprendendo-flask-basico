from flask import Flask, json, render_template, request, abort, jsonify
from werkzeug.exceptions import HTTPException
from database import db
from models import Usuario
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db.init_app(app)
@app.route('/')
def home():
    return '<h1>home do site</h1>'
@app.route('/par_ou_impar/<int:numero>')
def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'<h1>{numero} é par</h1>'
    else:
        return f'<h1>{numero} é ímpar</h1>'
@app.errorhandler(Exception)
def manipular_excessao(e):
    if isinstance(e, HTTPException):
        return e
    return render_template('500_generico.html', e=e), 500
def pegar_usuario(username):
    user = db.session.query(Usuario).filter_by(nome=username).first()
    return user
@app.route('/perfil')
def perfil_do_usuario():
    username =  request.args.get('username').title()
    print(username)
    if username is None:
        abort(400)
    user = pegar_usuario(username=username)
    if user is None:
        abort(404)
    return render_template('perfil.html', username=username)
class UsoInvalidoDaAPI(Exception):
    codigo_do_status = 400
    def __init__(self, mensagem, codigo_do_status=None, payload = None):
        super().__init__()
        self.mensagem = mensagem
        if codigo_do_status is not None:
            self.codigo_do_status = codigo_do_status
        self.payload = payload
    def para_dict(self):
        rv = dict(self.payload or ())
        rv['mensagem'] = self.mensagem
        return rv 
@app.errorhandler(UsoInvalidoDaAPI)
def uso_invalido_da_api(e):
    return jsonify(e.para_dict()), e.codigo_do_status
def obter_usuario(id_do_usuario):
    usuario = db.session.query(Usuario).filter_by(id=id_do_usuario).first()
    return usuario
@app.route('/api/usuario')
def usuario_da_api():
    id_do_usuario = request.args.get('id_do_usuario')
    if not id_do_usuario:
        raise UsoInvalidoDaAPI('nenhum usuário foi fornecido!')
    usuario = obter_usuario(id_do_usuario=id_do_usuario)
    if not usuario:
        raise UsoInvalidoDaAPI('esse usuário não existe!', codigo_do_status=404)
    return jsonify(usuario.para_dict())
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
