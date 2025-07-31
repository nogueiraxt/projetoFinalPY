# Gerenciador de Tarefas

Este projeto é um aplicativo simples de gerenciamento de tarefas com interface gráfica, desenvolvido em Python. Ele permite que o usuário adicione, visualize, edite e remova tarefas, salvando todas as informações em um banco de dados MySQL.

## Recursos
- Adicionar novas tarefas com descrição, data de início, data de término e status.
- Visualizar todas as tarefas em uma tabela.
- Editar detalhes de uma tarefa existente.
- Marcar tarefas como "Concluída".
- Remover todas as tarefas concluídas de uma só vez.

## Tecnologias
- **Python:** Linguagem de programação principal.
- **Tkinter:** Biblioteca padrão do Python para a criação da interface gráfica.
- **tkcalendar:** Widget para seleção de datas na interface gráfica.
- **mysql-connector-python:** Driver para conexão com o banco de dados MySQL.

## Pré-requisitos
Antes de rodar a aplicação, você precisa ter o seguinte instalado:
- **Python 3.x**
- **Servidor MySQL**

## Configuração do Banco de Dados
Para que a aplicação funcione corretamente, você deve configurar o banco de dados MySQL:
1. Abra um cliente MySQL (como MySQL Workbench, DBeaver ou a linha de comando).
2. Execute o script `scripts.sql` que está na raiz do projeto. Este script irá criar o banco de dados `todo` e a tabela `tarefas`.

## Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/nogueiraxt/gerenciador-de-tarefas.git
    cd gerenciador-de-tarefas
    ```

2.  **Instale as dependências Python:**
    ```bash
    pip install tkcalendar
    pip install mysql-connector-python
    ```

3.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

A janela do aplicativo de gerenciamento de tarefas será exibida, e você poderá começar a usar!
