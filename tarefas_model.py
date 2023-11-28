import datetime
import uuid


class Tarefa:
    def __init__(self, descricao, data_inicio, data_termino, status):
        self.id = str(uuid.uuid4())
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.status = status


def criar_tarefa(descricao, data_inicio, data_termino, status):
    return Tarefa(descricao, data_inicio, data_termino, status)
