from flask import Blueprint
calculadora_bp = Blueprint('calculadora', __name__)
@calculadora_bp.route('/somar/<int:n1>/<int:n2>')
def somar(n1,n2):
    res = n1+n2
    return f'resultado: {res}'
@calculadora_bp.route('/subtrair/<int:n1>/<int:n2>')
def subtrair(n1,n2):
    res = n1-n2
    return f'resultado: {res}'