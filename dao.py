import sqlite3

# Função para criar a tabela "candidatos" no banco de dados SQLite
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidato (
                    id_candidato INTEGER PRIMARY KEY, -- 0
	                nome TEXT NOT NULL, -- 1
	                idade INTEGER, -- 2
	                cidade TEXT, -- 3
                    estado TEXT, -- 4
                    telefone TEXT, -- 5
                    email TEXT, -- 6
                    linkedin TEXT, -- 7
                    status_candidato TEXT, -- 8
                    pretensao_salarial REAL, -- 9
                    area_trabalho TEXT, -- 10 backend, frontend, fullstack
                    soft_skills TEXT, -- 11
                    hard_skills TEXT, -- 12
                    outra_informacao TEXT, -- 13
                    nome_arquivo TEXT, -- 14
                    curriculo_data BLOB -- 15
                   )''')
    conn.commit()
    conn.close()

# Função para inserir um novo candidato na tabela
def inserir_candidato(campos):
    nome = campos['nome'].get()
    idade = campos['idade'].get()
    cidade = campos['cidade'].get()
    estado = campos['estado'].get()
    telefone = campos['telefone'].get()
    email = campos['email'].get()
    linkedin = campos['linkedin'].get()
    soft_skills = campos['soft_skills'].get(1.0, "end-1c")
    hard_skills = campos['hard_skills'].get(1.0, "end-1c")
    outra_informacao = campos['outra_informacao'].get(1.0, "end-1c")
    
    pretensao_salarial = campos['pretensao_salarial'].get()
    area_trabalho = campos['area_trabalho'].get()
    status_candidato = campos['status_candidato'].get()
    if status_candidato == '':
        status_candidato = 'Em Espera'

    caminho_curriculo = campos['caminho_curriculo']
    print("Caminho do Arquivo: ", caminho_curriculo)
    with open(caminho_curriculo, 'rb') as curriculo_file:
            curriculo_data = curriculo_file.read()

    conn = conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO candidato (nome, idade, cidade, estado, telefone, email, 
                                            linkedin, status_candidato, pretensao_salarial, 
                                            area_trabalho, soft_skills, hard_skills, 
                                            outra_informacao, nome_arquivo, curriculo_data) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (
                       nome, idade, cidade, estado, telefone, email, 
                                            linkedin, status_candidato, pretensao_salarial, 
                                            area_trabalho, soft_skills, hard_skills, 
                                            outra_informacao, caminho_curriculo, curriculo_data
                       ))
    conn.commit()
    conn.close()
    return True

# Função para atualizar status do candidato
def atualizar_status(id_candidato, novo_status):
    conn = conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE candidato SET status_candidato = ? WHERE id_candidato = ?", (novo_status, id_candidato,))
    conn.commit()
    conn.close()
    return True

# Função para listar todos os candidatos na tabela
def listar_candidatos(nome, email, cidade, estado, faixa_inicial, faixa_final, area, status_candidato):

    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM candidato WHERE 1 = 1 "
    if nome:
        query += " AND LOWER(nome) like '%" + nome.lower() + "%'"
    if email:
        query += " AND LOWER(email) like '%" + email.lower() + "%'"
    if cidade:
        query += " AND LOWER(cidade) like '%" + cidade.lower() + "%'"
    if estado:
        query += " AND LOWER(estado) like '%" + estado.lower() + "%'"
    if area and area != 'Todos':
        query += " AND area_trabalho = '" + area + "'"
    if status_candidato and status_candidato != 'Todos':
        query += " AND status_candidato = '" + status_candidato + "'"
    if faixa_inicial: 
        if faixa_final:
            query += " AND pretensao_salarial >=" + faixa_inicial + " AND pretensao_salarial <=" + faixa_final
        else:
            query += " AND pretensao_salarial >=" + faixa_inicial 

    cursor.execute(query)

    lista = cursor.fetchall()
    conn.close()
    if lista:
        return lista
    else:
        return []

# Função para consultar um candidado por id
def consulta(id_candidato):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM candidato WHERE id_candidato = ?", (id_candidato,))
    candidato = cursor.fetchone()
    conn.close()

    if candidato:
        return {
            'id_candidato': candidato[0],
            'nome': candidato[1],
            'idade': candidato[2],
            'cidade': candidato[3],
            'estado': candidato[4],
            'telefone': candidato[5],
            'email': candidato[6],
            'linkedin': candidato[7],
            'status_candidato': candidato[8],
            'pretensao_salarial': candidato[9],
            'area_trabalho': candidato[10],
            'soft_skills': candidato[11],
            'hard_skills': candidato[12],
            'outra_informacao': candidato[13],
            'nome_arquivo': candidato[14],
            'curriculo_data': candidato[15]
        }
    else:
        return None

# Conecta ao banco de dados
def conectar():
    return sqlite3.connect('database/db-trabalho')