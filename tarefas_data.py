import mysql.connector
from mysql.connector import Error
import uuid


def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="todo"
        )
        return conexao
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id VARCHAR(100) NOT NULL UNIQUE,
                descricao VARCHAR(100) NOT NULL,
                dtini DATE NOT NULL,
                dtfim DATE NOT NULL,
                status VARCHAR(100) NOT NULL
            )
        """)
        conexao.commit()
        cursor.close()
    except Error as e:
        print("Erro ao criar a tabela:", e)


def salvar_tarefa_bd(descricao, data_inicio, data_termino, status):
    try:
        conexao = conectar_bd()
        if conexao is not None:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO tarefas (id, descricao, dtini, dtfim, status) VALUES (%s, %s, %s, %s, %s)",
                           (str(uuid.uuid4()), descricao, data_inicio, data_termino, status))
            conexao.commit()
            cursor.close()
            conexao.close()
            return True
    except Error as e:
        print("Erro ao salvar a tarefa no banco de dados:", e)
        return False


def carregar_dados_bd():
    try:
        conexao = conectar_bd()
        if conexao is not None:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tarefas")
            dados = cursor.fetchall()
            cursor.close()
            conexao.close()
            return dados
    except Error as e:
        print("Erro ao carregar os dados do banco de dados:", e)
        return []


def remover_tarefas_concluidas_bd():
    try:
        conexao = conectar_bd()
        if conexao is not None:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM tarefas WHERE status = 'Concluída'")
            conexao.commit()
            cursor.close()
            conexao.close()
            return True
    except Error as e:
        print("Erro ao remover tarefas concluídas do banco de dados:", e)
        return False


def editar_tarefa_bd(tarefa_id, nova_descricao, nova_data_inicio, nova_data_termino, novo_status):
    try:
        conexao = conectar_bd()
        if conexao is not None:
            cursor = conexao.cursor()
            cursor.execute("""
                UPDATE tarefas
                SET descricao = %s, dtini = %s, dtfim = %s, status = %s
                WHERE id = %s
            """, (nova_descricao, nova_data_inicio, nova_data_termino, novo_status, tarefa_id))
            conexao.commit()
            cursor.close()
            conexao.close()
            return True
    except Error as e:
        print("Erro ao editar a tarefa no banco de dados:", e)
        return False
