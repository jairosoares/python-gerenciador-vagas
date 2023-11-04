import tkinter as tk
from tkinter import ttk,messagebox
from dao import consulta, atualizar_status

def criar_modal(root, id_candidato):
    i = 0
    largura = 40
    candidato = consulta(id_candidato)
    modal = define_modal(root)

    # Crie um quadro para os campos do modal
    frame_modal = tk.Frame(modal)
    frame_modal.grid(row=0, column=0, sticky="w", padx=10, pady=30)

    i += 1
    tk.Label(frame_modal, text="Nome: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['nome']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Idade: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['idade']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Cidade: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['cidade']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Estado: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['estado']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Telefone: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['telefone']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="E-mail: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['email']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Prensão Salarial: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['pretensao_salarial']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Soft Skills: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['soft_skills']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Hard Skills: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['hard_skills']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Complemento: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['outra_informacao']).grid(row=i, column=1, sticky="w")

    i += 1
    tk.Label(frame_modal, text="Área de Trabalho: ").grid(row=i, column=0)
    tk.Label(frame_modal, text=candidato['area_trabalho']).grid(row=i, column=1, sticky="w")

    i += 1
    ttk.Label (frame_modal, text = "Status:", font = ("Times New Roman", 10)).grid (row=i, column=0, padx=10, pady=25)
    n = tk.StringVar ()
    status_combo = ttk.Combobox (frame_modal, width = largura - 4, textvariable = n)
    status_combo ['values'] = ('Em Espera',  'Aprovado','Reprovado')
    status_combo.grid (row = i, column = 1)

    i += 1
    atualizar_button = tk.Button(frame_modal, text="Atualizar Status", width=15, command = lambda: atualiza_status(candidato, modal, status_combo.get()))
    atualizar_button.grid(row=i, column=1, sticky="e")

    # Após o carregamento completo do modal, defina o valor do Combobox
    root.after(1, lambda: status_combo.set(candidato['status_candidato']))

    return modal

def atualiza_status(candidato, modal, novo_status):
    print(">atualizando ", novo_status)
    atualizar_status(candidato['id_candidato'], novo_status)
    resultado = messagebox.showinfo("Mensagem", "Status do candidato foi atualizado com sucesso")
    if resultado:
        modal.destroy()

def define_modal(root):
    modal = tk.Toplevel(root)
    modal.title("Detalhes do Candidato")

    # Calcula a largura e a altura do modal
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    largura_modal = largura_tela * 0.5  # 70% da largura da tela principal
    altura_modal = altura_tela * 0.5  # 70% da altura da tela principal

    # Configura a geometria do modal para centralizá-lo e definir o tamanho
    x = (largura_tela - largura_modal) / 2
    y = (altura_tela - altura_modal) / 2
    modal.geometry(f"{int(largura_modal)}x{int(altura_modal)}+{int(x)}+{int(y)}")
    return modal
