from flask_restful import Resource
from ..schemas import conta_schema
from flask import request, make_response, jsonify
from ..entities import conta
from ..services import conta_service
from api import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..decorators.autorizacao import user_conta
from ..decorators.api_key import require_apikey

class ContaList(Resource):

    @jwt_required()
    def get(self):
        usuario_logado = get_jwt_identity()
        contas = conta_service.listar_contas(usuario=usuario_logado)
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 201)

    @jwt_required()
    def post(self):
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, valor=valor)
            resultado = conta_service.cadastrar_conta(conta_nova)
            return make_response(cs.jsonify(resultado), 201)

class ContaDetail(Resource):

    @user_conta
    def get(self, id):
        conta = conta_service.listar_contas_id(id)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)

    @user_conta
    def put(self, id):
        conta_bd = conta_service.listar_contas_id(id)
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome, valor=valor)
            resultado = conta_service.atualizar_conta(conta_bd, conta_nova)
            return make_response(cs.jsonify(resultado), 201)

    @user_conta
    def delete(self, id):
        conta = conta_service.listar_contas_id(id)
        conta_service.excluir_conta(conta)
        return make_response(jsonify(""), 204)


api.add_resource(ContaList, '/contas')
api.add_resource(ContaDetail, '/contas/<int:id>')