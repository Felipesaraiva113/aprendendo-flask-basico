from database import db
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True)
    def para_dict(self):
        return {'id': self.id, 'nome': self.nome}
