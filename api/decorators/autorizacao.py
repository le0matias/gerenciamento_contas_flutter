from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..services import conta_service
from flask import make_response, jsonify

def user_conta(view_function):
    @wraps(view_function)
    def decorator_function(*args, **kwargs):
        verify_jwt_in_request()
        usuario_logado = get_jwt_identity()
        conta = conta_service.listar_contas_id(kwargs['id'])
        if conta is None:
            return make_response(jsonify("Conta nao encontrada"), 404)
        elif conta.usuario_id == usuario_logado:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify("Esta conta nao pertence ao usuario logado"), 403)
    return decorator_function