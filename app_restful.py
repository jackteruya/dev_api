from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, lista_habilidades, ListaHabilidade

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
         'id':'0',
         'nome':'Jackson',
         'habilidades':['Python','Flask']
     },
    {
         'id':'1',
         'nome':'Teruya',
         'habilidades':['Python','Django']}
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'satatus':'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Regsitro excluído'}

# Lista tods os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        dados_validados = [validar for validar in lista_habilidades if validar in dados['habilidades']]
        if len(dados_validados) == len(dados['habilidades']):
            posicao = len(desenvolvedores)
            dados['id']=posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]
        else:
            mensagem = 'Habilidade nao cadastrada!'
            return {'status':'erro','mensagem':mensagem, 'habilidades':lista_habilidades}


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(ListaHabilidade, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)