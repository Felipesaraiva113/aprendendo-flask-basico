from flask import Flask,render_template,url_for,redirect,request
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db = SQLAlchemy()
db.init_app(app)
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer,primary_key=True)
    nome= db.Column(db.String(40),nullable=False,unique=True)

@app.route('/')
def homepage():
    dados = {'nome': 'felipe'}
    return render_template('homepage.html', dados=dados)
@app.route('/contatos')
def contatos():
    contatos = ['mário','bruno','pedro','thiago']
    return render_template('contatos.html', contatos=contatos)
@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html',nome_usuario=nome_usuario,idade=19)
@app.route('/usuarios/')
def sem_usuario():
    return render_template('usuarios.html',nome_usuario=None)
@app.route('/formulario',methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome=request.form['nomeForm']
        email = request.form['emailForm']
        print(f'nome: {nome}')
        print(f'email: {email}')
    return render_template('formularios.html')
if __name__ == '__main__':
    with app.app_context():
        user = Usuario(nome='Felipe')
        db.session.add(user)
        db.session.commit()
        db.create_all()
    app.run(debug=True) 

