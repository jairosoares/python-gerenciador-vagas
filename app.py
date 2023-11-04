import tkinter as tk
from tkinter import ttk
from dao import criar_tabela
import cadastro, gestao

criar_tabela()

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciamento de Vagas")
root.state('zoomed')

# Cria um estilo personalizado para o Notebook
style = ttk.Style()
style.configure("Custom.TNotebook.Tab", background="lightgray", padding=[10, 5])
style.configure("Custom.TNotebook.Tab", background="lightgray", borderwidth=2)
style.map("Custom.TNotebook.Tab", background=[("selected", "gray40")], borderwidth=[("selected", 2)])

# Cria notebook para as abas
notebook = ttk.Notebook(root, style="Custom.TNotebook")
notebook.pack(fill='both', expand=True)

# Aba 1: Candidato
candidato_frame = ttk.Frame(notebook)
notebook.add(candidato_frame, text='Candidato')
cadastro.criar_aba(candidato_frame)

# Aba 2: Gestao
gestao_frame = ttk.Frame(notebook)
notebook.add(gestao_frame, text='Gestão')
gestao.criar_aba(gestao_frame)

root.mainloop()