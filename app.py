import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tarefas_data import carregar_dados_bd, salvar_tarefa_bd, editar_tarefa_bd, remover_tarefas_concluidas_bd
from tarefas_model import criar_tarefa


def on_tarefa_selecionada(event):
    selected_item = tree.selection()

    if selected_item:
        item_values = tree.item(selected_item, 'values')

        entry_descricao.delete(0, tk.END)
        entry_descricao.insert(0, item_values[1])

        data_inicio = converter_data_para_dateentry_format(item_values[2])
        data_termino = converter_data_para_dateentry_format(item_values[3])

        entry_inicio.set_date(data_inicio)
        entry_termino.set_date(data_termino)

        combo_status.set(item_values[4])


def converter_data_para_dateentry_format(data_string):
    data_obj = datetime.strptime(data_string, '%Y-%m-%d')
    return data_obj.strftime('%d/%m/%Y')


def salvar_tarefa():
    descricao = entry_descricao.get()
    data_inicio = entry_inicio.get_date().strftime('%Y-%m-%d')
    data_termino = entry_termino.get_date().strftime('%Y-%m-%d')
    status = combo_status.get()

    if salvar_tarefa_bd(descricao, data_inicio, data_termino, status):
        atualizar_tabela()


def remover_tarefas_concluidas():
    if remover_tarefas_concluidas_bd():
        atualizar_tabela()


def editar_tarefa():
    selected_item = tree.selection()

    if selected_item:
        tarefa_id = tree.item(selected_item, 'values')[0]

        nova_descricao = entry_descricao.get()
        nova_data_inicio = entry_inicio.get_date().strftime('%Y-%m-%d')
        nova_data_termino = entry_termino.get_date().strftime('%Y-%m-%d')
        novo_status = combo_status.get()

        if editar_tarefa_bd(tarefa_id, nova_descricao, nova_data_inicio, nova_data_termino, novo_status):
            atualizar_tabela()


def atualizar_tabela():
    for row in tree.get_children():
        tree.delete(row)

    dados = carregar_dados_bd()
    for row in dados:
        tree.insert("", "end", values=(row['id'], row['descricao'], row['dtini'], row['dtfim'], row['status']))


root = tk.Tk()
root.title("Cadastro de Tarefas")
root.configure(bg="black")
element_text_color = "white"

label_descricao = tk.Label(root, text="Descrição da Tarefa:", bg="black", fg=element_text_color)
entry_descricao = tk.Entry(root, bg="white", fg="black")

label_inicio = tk.Label(root, text="Data de Início:", bg="black", fg=element_text_color)
entry_inicio = DateEntry(root, width=12, background='darkred', foreground='white', borderwidth=2,
                         date_pattern='dd/mm/yyyy')

label_termino = tk.Label(root, text="Data de Término:", bg="black", fg=element_text_color)
entry_termino = DateEntry(root, width=12, background='darkred', foreground='white', borderwidth=2,
                          date_pattern='dd/mm/yyyy')

label_status = tk.Label(root, text="Status:", bg="black", fg=element_text_color)
status_options = ["A fazer", "Concluída", "Em andamento"]
combo_status = ttk.Combobox(root, values=status_options, style="TCombobox", background='white', foreground='black')

label_descricao.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_descricao.grid(row=0, column=1, padx=10, pady=10)

label_inicio.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_inicio.grid(row=1, column=1, padx=10, pady=10)

label_termino.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_termino.grid(row=2, column=1, padx=10, pady=10)

label_status.grid(row=3, column=0, padx=10, pady=10, sticky="w")
combo_status.grid(row=3, column=1, padx=10, pady=10)

botoes_frame = tk.Frame(root, bg="black")
botoes_frame.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

botao_atualizar = tk.Button(botoes_frame, text="Atualizar", command=atualizar_tabela, bg="red", fg="white", width=20)
botao_atualizar.grid(row=0, column=0, pady=5)

botao_adicionar = tk.Button(botoes_frame, text="Adicionar Tarefa", command=salvar_tarefa, bg="red", fg="white",
                            width=20)
botao_adicionar.grid(row=1, column=0, pady=5)

botao_editar = tk.Button(botoes_frame, text="Editar Tarefa", command=editar_tarefa, bg="red", fg="white", width=20)
botao_editar.grid(row=2, column=0, pady=5)

botao_remover_concluidas = tk.Button(botoes_frame, text="Remover Tarefas Concluídas",
                                     command=remover_tarefas_concluidas, bg="red", fg="white", width=20)
botao_remover_concluidas.grid(row=3, column=0, pady=5)

tree = ttk.Treeview(root, columns=("id", "descricao", "dtini", "dtfim", "status"), show="headings", style="Treeview")
tree.heading("id", text="ID")
tree.heading("descricao", text="Descrição")
tree.heading("dtini", text="Data Início")
tree.heading("dtfim", text="Data Término")
tree.heading("status", text="Status")
tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

style = ttk.Style(root)
style.theme_use("default")

style.configure("Treeview", background="white", fieldbackground="white", foreground="black")
style.map("Treeview", background=[("selected", "darkred")])

tree.bind("<ButtonRelease-1>", on_tarefa_selecionada)
atualizar_tabela()

root.mainloop()
