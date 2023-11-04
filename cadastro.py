import tkinter as tk
from tkinter import ttk,messagebox,filedialog
import re
from dao import inserir_candidato

# Cria a Aba Cadastro
def criar_aba(root):
    largura = 40
    campos = {}
    i = 0

    # Componentes da interface
    frame_cadastro = tk.Frame(root)
    frame_cadastro.grid(row=0, column=0, sticky="w", padx=10, pady=30)

    tk.Label(frame_cadastro, text="Nome *:").grid(row=i, column=0)
    nome_entry = tk.Entry(frame_cadastro, width=largura)
    nome_entry.grid(row=i, column=1)
    campos['nome'] = nome_entry

    i += 1
    tk.Label(frame_cadastro, text="Idade:").grid(row=i, column=0)
    idade_entry = tk.Entry(frame_cadastro, width=largura)
    idade_entry.grid(row=i, column=1)
    campos['idade'] = idade_entry

    i += 1
    tk.Label(frame_cadastro, text="Cidade:").grid(row=i, column=0)
    cidade_entry = tk.Entry(frame_cadastro, width=largura)
    cidade_entry.grid(row=i, column=1)
    campos['cidade'] = cidade_entry

    i += 1
    tk.Label(frame_cadastro, text="Estado:").grid(row=i, column=0)
    estado_entry = tk.Entry(frame_cadastro, width=largura)
    estado_entry.grid(row=i, column=1)
    campos['estado'] = estado_entry

    i += 1
    tk.Label(frame_cadastro, text="Telefone:").grid(row=i, column=0)
    telefone_entry = tk.Entry(frame_cadastro, width=largura)
    telefone_entry.grid(row=i, column=1)
    campos['telefone'] = telefone_entry

    i += 1
    tk.Label(frame_cadastro, text="E-mail *:").grid(row=i, column=0)
    email_entry = tk.Entry(frame_cadastro, width=largura)
    email_entry.grid(row=i, column=1)
    campos['email'] = email_entry
    campos['email'] = email_entry

    i += 1
    tk.Label(frame_cadastro, text="Lindekin:").grid(row=i, column=0)
    linkedin_entry = tk.Entry(frame_cadastro, width=largura)
    linkedin_entry.grid(row=i, column=1)
    campos['linkedin'] = linkedin_entry

    i += 1
    tk.Label(frame_cadastro, text="Pretensão Salarial *:").grid(row=i, column=0)
    pretensao_salario_entry = tk.Entry(frame_cadastro, width=largura)
    pretensao_salario_entry.grid(row=i, column=1)
    campos['pretensao_salarial'] = pretensao_salario_entry

    i += 1
    tk.Label(frame_cadastro, text="Soft Skill:").grid(row=i, column=0)
    soft_skill_text = tk.Text(frame_cadastro, height=4, width = largura - 10)
    soft_skill_text.grid(row=i, column=1)
    campos['soft_skills'] = soft_skill_text

    i += 1
    tk.Label(frame_cadastro, text="Hard Skill:").grid(row=i, column=0)
    hard_skill_text = tk.Text(frame_cadastro, height=4, width = largura - 10)
    hard_skill_text.grid(row=i, column=1)
    campos['hard_skills'] = hard_skill_text

    i += 1
    tk.Label(frame_cadastro, text="Complemento:").grid(row=i, column=0)
    complemento_skill_text = tk.Text(frame_cadastro, height=4, width = largura - 10)
    complemento_skill_text.grid(row=i, column=1)
    campos['outra_informacao'] = complemento_skill_text

    # Upload do curriculo
    i += 1
    tk.Label(frame_cadastro, text="Currículo *:").grid(row=i, column=0)
    upload_button = tk.Button(frame_cadastro, text="Fazer Upload", command=lambda: fazer_upload(campos))
    upload_button.grid(row=i, column=1)
    campos['curriculo'] = upload_button  
    i += 1
    caminho_curriculo_label = tk.Label(frame_cadastro, text="...", wraplength=300)
    caminho_curriculo_label.grid(row=i, column=1)
    campos['caminho_curriculo_label'] = caminho_curriculo_label
    campos['caminho_curriculo'] = ""

    i += 1
    ttk.Label (frame_cadastro, text = "Área Trabalho *:", font = ("Times New Roman", 10)).grid (row=i, column=0, padx=10, pady=25)
    n = tk.StringVar ()
    area_combo = ttk.Combobox (frame_cadastro, width = largura - 3, textvariable = n)
    area_combo ['values'] = ('Bakend',  'Frontend','Fullstrack')
    area_combo.grid (row = i, column = 1)
    area_combo.current ()
    campos['area_trabalho'] = area_combo

    i += 1
    ttk.Label (frame_cadastro, text = "Status:", font = ("Times New Roman", 10)).grid (row=i, column=0, padx=10, pady=25)
    n = tk.StringVar ()
    status_combo = ttk.Combobox (frame_cadastro, width = largura - 4, textvariable = n)
    status_combo ['values'] = ('Em Espera',  'Aprovado','Reprovado')
    status_combo.grid (row = i, column = 1)
    status_combo.current ()
    campos['status_candidato'] = status_combo

    i += 1
    inserir_button = tk.Button(frame_cadastro, text="Inserir Candidato", command=lambda: inserir_registro(campos))
    inserir_button.grid(row=i, column=1, columnspan=20)

def inserir_registro(campos):
    if valida_campos_obrigatorio(campos):
        if valida_email(campos['email'].get()):
            inserir_candidato(campos)
            messagebox.showinfo("Mensagem", "Candidato inserido com sucesso!\nVá na Aba Gestão para consultar candidatos.")
            limpar_campos(campos)
        else:
            messagebox.showwarning("Alerta", "E-mail inválido. Informe um e-mail válido.")
    else:
        messagebox.showwarning("Alerta", "Informe os campos obrigatórios!")

def valida_campos_obrigatorio(campos):
    nome = campos['nome'].get()
    email = campos['email'].get()
    pretensao_salarial = campos['pretensao_salarial'].get()
    area_trabalho = campos['area_trabalho'].get()
    caminho_curriculo = campos['caminho_curriculo']
    
    # Verifique se algum campo obrigatório está em branco
    if nome == "" or email == "" or pretensao_salarial == "" or area_trabalho == "" or caminho_curriculo == "":
        return False
    
    return True

def valida_email(email):
    # Verifique se o campo de e-mail tem um formato válido
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

def fazer_upload(campos):
    # Abra uma caixa de diálogo para selecionar o arquivo do currículo
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])

    if arquivo:
        # Mostra uma mensagem de sucesso e exibe o nome do arquivo
        print("Arquivo selecionado com sucesso:", arquivo)
        campos['caminho_curriculo_label'].config(text=arquivo)
        campos['caminho_curriculo'] = arquivo
        messagebox.showinfo("Upload de Currículo", f"Upload bem-sucedido!\n{arquivo}")
    else:
        campos['caminho_curriculo'] = ""
        messagebox.showinfo("Upload de Currículo", "Nenhum arquivo selecionado.")

def limpar_campos(campos):
    campos["caminho_curriculo"] = ""
    if "caminho_curriculo_label" in campos:
        campos["caminho_curriculo_label"].config(text="")
    # Limpa todos os outros campos    
    for chave, widget in campos.items():
        if isinstance(widget, (tk.Entry, ttk.Combobox)):
            widget.delete(0, "end")
        elif isinstance(widget, tk.Text):
            widget.delete(1.0, "end")
