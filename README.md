# Gerenciador de Vagas

Submissão do perfil de desenvolvedores (Candidato) e avaliação por recrutador (Gestão)

## Estrutura de arquivos do projeto

- `app.py`: Contém os componentes das abas.
- `cadastro.py`: Componentes da aba Candidato
- `gestao.py`: Componentes da aba Gestão
- `gestaomodal.py`: Componentes modal ao clicar em detalhes do candidato
- `dao.py`: Componente responsável pela comunicação com o banco de dados SQLite

## Princípios de Design

Procurei criar o projeto seguindo os princípios de design:

- **Clean Code**: O código é legível, coeso e segue as convenções da linguagem.
- **Modularização**: O código está organizado em módulos reutilizáveis.
- **Documentação**: O código e a API estão bem documentados.
- **Manutenibilidade**: O projeto é projetado para ser facilmente mantido e expandido.

## Requisitos

- Criar uma interface gráfica que suporte a submissão dos dados por parte do usuário e salve essas informações em um banco de dados para possível futura consulta. Sendo eles: Dados principais do usuário: nome, idade, cidade e estado onde mora, telefone e e-mail. 
Experiências: com o que já trabalhou,principais soft skills e hard skills, linkedIn;
Empregabilidade: Status atual de emprego, expectativa salarial e outras informações que podemos precisar; Além disso, é importante abrir um espaço para que seja submetido o currículo atual em pdf ou word e armazená-lo também ao banco. 
- Criar uma interface gráfica para os gestores da vaga, que permite com que o recrutador, veja os candidatos cadastrados, aplique filtro por cidade, estado, por expectativa salarial, ou área de trabalho (comercial, atendimento e etc).  Ele também precisa, caso necessite entrar em contato com a pessoa, ver esses contatos. E pode atribuir um status de já aprovado, reprovado e em espera. 



## Autor

- [Jairo Soares] - [202211446202@alunos.estacio.br]

## Agradecimento

- Professor Gesse Evangelista
