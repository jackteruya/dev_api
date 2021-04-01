from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP', 'Django', 'JavaScript']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades