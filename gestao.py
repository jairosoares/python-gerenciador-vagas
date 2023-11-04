import tkinter as tk
from tkinter import ttk,messagebox
import webbrowser
from dao import listar_candidatos
from gestaomodal import criar_modal

# Cria a Aba Gestao
def criar_aba(root):
    largura = 40
    campos = {}
    i = 0

    # Crie um quadro para os campos de pesquisa
    frame_pesquisa = tk.Frame(root)
    frame_pesquisa.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    
    tk.Label(frame_pesquisa, text="Nome:").grid(row= i, column=0)
    nome_entry = tk.Entry(frame_pesquisa, width=largura)
    nome_entry.grid(row=i, column=1)
    campos['nome'] = nome_entry

    i += 1
    tk.Label(frame_pesquisa, text="E-mail:").grid(row= i, column=0)
    email_entry = tk.Entry(frame_pesquisa, width=largura)
    email_entry.grid(row=i, column=1)
    campos['email'] = email_entry

    i += 1
    tk.Label(frame_pesquisa, text="Cidade:").grid(row= i, column=0)
    cidade_entry = tk.Entry(frame_pesquisa, width=largura)
    cidade_entry.grid(row=i, column=1)
    campos['cidade'] = cidade_entry

    i += 1
    tk.Label(frame_pesquisa, text="Estado:").grid(row= i, column=0)
    estado_entry = tk.Entry(frame_pesquisa, width=largura)
    estado_entry.grid(row=i, column=1)
    campos['estado'] = estado_entry

    i += 1
    tk.Label(frame_pesquisa, text="Faixa Salarial:").grid(row= i, column=0)
    faixa_inicial_entry = tk.Entry(frame_pesquisa, width=18)
    faixa_inicial_entry.grid(row=i, column=1, sticky="w")
    campos['faixa_inicial'] = faixa_inicial_entry

    faixa_final_entry = tk.Entry(frame_pesquisa, width=18)
    faixa_final_entry.grid(row=i, column=1, sticky="e")
    campos['faixa_final'] = faixa_final_entry

    i += 1
    ttk.Label (frame_pesquisa, text = "Área Trabalho *:", font = ("Times New Roman", 10)).grid (row=i, column=0, padx=10, pady=25)
    n = tk.StringVar ()
    area_combo = ttk.Combobox (frame_pesquisa, width = largura - 3, textvariable = n)
    area_combo ['values'] = ('Bakend',  'Frontend','Fullstrack', 'Todos')
    area_combo.grid (row = i, column = 1)
    area_combo.current ()
    campos['area'] = area_combo

    i += 1
    ttk.Label (frame_pesquisa, text = "Status *:", font = ("Times New Roman", 10)).grid (row=i, column=0, padx=10, pady=25)
    n = tk.StringVar ()
    status_combo = ttk.Combobox (frame_pesquisa, width = largura - 3, textvariable = n)
    status_combo ['values'] = ('Em Espera',  'Aprovado','Reprovado', 'Todos')
    status_combo.grid (row = i, column = 1)
    status_combo.current ()
    campos['status_candidato'] = status_combo

    i += 1
    listar_button = tk.Button(frame_pesquisa, text="Listar Candidato", width=15, command = lambda: montar_candidatos(
        root,
        table_frame,
        listar_button,
        nome_entry.get(),
        email_entry.get(),
        cidade_entry.get(),
        estado_entry.get(),
        faixa_inicial_entry.get(),
        faixa_final_entry.get(),
        area_combo.get(),
        status_combo.get()
        ))
    listar_button.grid(row=i, column=1, sticky="w")

    limpar_button = tk.Button(frame_pesquisa, text="Limpar", width=15, command = lambda: limpar_campos(table_frame, campos))
    limpar_button.grid(row=i, column=1, sticky="e")
    # Quadro para a tabela
    
    i += 3
    table_frame = tk.Frame(root)
    table_frame.grid(row=i, column=0)

def limpar_campos(table_frame, campos):
    # Limpando os campos
    for chave, widget in campos.items():
        if isinstance(widget, (tk.Entry, ttk.Combobox)):
            widget.delete(0, "end")
        elif isinstance(widget, tk.Text):
            widget.delete(1.0, "end")
    
    # Limpando a grid
    for widget in table_frame.winfo_children():
        widget.destroy()

# Função para listar todos os alunos na tabela
def montar_candidatos(root, table_frame, listar_button, nome, email, cidade, estado, faixa_inicial, faixa_final, area, status_candidato):
    print("> Montando lista de candidatos...")
    candidatos = listar_candidatos(nome, email, cidade, estado, faixa_inicial, faixa_final, area, status_candidato)

    # Limpa a tabela existente
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Largura das colunas
    larguras = [20, 30, 20, 20, 15, 13, 12, 12, 12]

    # Cabeçalho da tabela
    header_labels = ['Nome', 'E-mail', 'Cidade', 'Estado', 'Pretensao Salarial', 'Área Trabalho', 'Status', 'Currículo', 'Detalhe']
    for col, label_text in enumerate(header_labels):
        tk.Label(table_frame, text=label_text, relief=tk.RIDGE, width=larguras[col]).grid(row=0, column=col)

    # Linhas da tabela
    for row, candidato in enumerate(candidatos, start=1):
        campos_a_exibir = [candidato[1], candidato[6], candidato[3], candidato[4], candidato[9], candidato[10], candidato[8], candidato[15], candidato[0]]
        for col, valor in enumerate(campos_a_exibir):
            if col == 7:  # Esta é a coluna do currículo
                link_label = tk.Label(table_frame, text="Abrir", fg="blue", cursor="hand2", relief=tk.RIDGE, width=larguras[col])
                link_label.grid(row=row, column=col)
                link_label.bind("<Button-1>", lambda event, caminho=candidato[15]: abrir_pdf(caminho))
            elif col == 8:
                link_label = tk.Label(table_frame, text="Consultar", fg="blue", cursor="hand2", relief=tk.RIDGE, width=larguras[col])
                link_label.grid(row=row, column=col)
                link_label.bind("<Button-1>", lambda event, id_candidato=candidato[0]: abrir_modal(root, listar_button, id_candidato))
            else:
                tk.Label(table_frame, text=valor, relief=tk.RIDGE, width=larguras[col]).grid(row=row, column=col)

def abrir_modal(root, listar_button, id_candidato):
    print("> chamou modal")
    modal = criar_modal(root, id_candidato)
    modal.transient(root)
    modal.grab_set()
    root.wait_window(modal)
    # Disparar o listar_button 
    if listar_button:
        listar_button.invoke()

# Função para abrir o arquivo PDF
def abrir_pdf(curriculo_data):
    if curriculo_data:
        try:
            # Salve os dados BLOB como um arquivo temporário (PDF)
            with open("temp_curriculo.pdf", "wb") as temp_file:
                temp_file.write(curriculo_data)

            # Abra o arquivo PDF em um navegador
            webbrowser.open("temp_curriculo.pdf")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir o PDF: {str(e)}")

    else:
        messagebox.showinfo("Informação", "Nenhum currículo encontrado para este candidato.")