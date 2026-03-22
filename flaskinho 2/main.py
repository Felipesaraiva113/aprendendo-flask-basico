from flask import Flask, render_template,url_for,request,make_response,abort,redirect
from markupsafe import escape
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
     return redirect(url_for('login'))
@app.route('/login',methods=['POST','GET'])
def login():
    abort(401)
    return render_template('login.html')
@app.route('/ola')
def ola_mundo():
    return render_template('olaMundo.html')
@app.route('/usuario/<usuario_nome>')
def mostrar_perfil_usuario(usuario_nome):
    return f'Usuário {escape(usuario_nome)}'
@app.route('/post/<int:post_id>')
def mostrar_post(post_id):
    return f'Post {escape(post_id)}'
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'
@app.route('/projetos/')
def projetos():
    return render_template('projetos.html')
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('mostrar_perfil_usuario',usuario_nome='John Watson')) 
@app.route('/oi/')
@app.route('/oi/<nome>')
def oi(nome=None):
    return render_template('oi.html', pessoa = nome)
with app.test_request_context('/ola',method='POST'):
    assert request.path == '/ola'
    assert request.method == 'POST'
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    resp= make_response(render_template('pagina_nao_encontrada.html'),404)
    resp.headers['x-alguma coisa'] = 'valor a'
    return resp
app.run(debug=True)