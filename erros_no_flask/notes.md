@app.errorhandler(400)
@app.errorhandler(404)
def tratar_erros_comuns(e):
    print(type(e))
    return f'ocorreu um erro: {e.name}', e.code
class ArmazenamentoInsuficiente(HTTPException):
    code = 507
    description = 'Não há espaço de armazenamento suficiente.'
def handle_507(e):
    return 'desculpe, nosso servidor está sem espaço.', 507
app.register_error_handler(ArmazenamentoInsuficiente, handle_507)
@app.route('/simular-erro')
def simular():
    raise ArmazenamentoInsuficiente()'''
'''@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        'código': e.code,
        'nome': e.name,
        'descrição': e.description,
    })
    response.content_type = 'application/json'
    return response