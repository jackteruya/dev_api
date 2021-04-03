from flask_restful import Resource, Api
from flask import Flask, request
import json

app = Flask(__name__)
api = Api(app)

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP', 'Django']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados['habilidade'])
        return lista_habilidades[len(lista_habilidades)-1]

class ListaHabilidade(Resource):
    def get(self, id):
        try:
            response = {'habilidade': lista_habilidades[id]}
        except IndexError:
            mensagem = 'Habilidade de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'satatus': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados['habilidade']
        return dados

    def delete(self, id):
        habilidade_deletada = lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Habilidade {} excluído'.format(habilidade_deletada)}

'''api.add_resource(Habilidades, '/habilidades/')
api.add_resource(ListaHabilidade, '/habilidades/<int:id>')'''

if __name__ == '__main__':
    app.run(debug=True)
