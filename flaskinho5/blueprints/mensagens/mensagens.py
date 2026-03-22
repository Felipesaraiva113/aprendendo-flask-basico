from flask import Blueprint, render_template
mensagens_bp = Blueprint('mensagens', __name__, template_folder='templates',static_folder='static',static_url_path='/mensagens/static')
@mensagens_bp.route('/ola')
def ola():
    return render_template('ola.html')
@mensagens_bp.route('/oi')
def oi():
    return 'oi!'
