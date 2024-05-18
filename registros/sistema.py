# Importando as funções e variáveis criadas no arquivo init.py para o arquivo .py principal
from registros import *

# Lista com as opções que serão passadas como parâmetro para a função menu()
opcoes = ['Ver Registro de Alunos', 'Cadastrar novo Aluno', 'Ver Apresentações Agendadas', 'Agendar nova Apresentação',
          'Sair do Sistema']

# Caso os arquivos necessários para registrar os dados não existam, cria automaticamente
if not existeArquivo(arqAlunos):
    criarArquivo(arqAlunos)
if not existeArquivo(arqApresentacoes):
    criarArquivo(arqApresentacoes)

# Loop infinito com o conteúdo do programa principal
while True:
    menu(opcoes)
    opcao = lerInt(f'{verde}Sua escolha: {limpaCor}')
    match opcao:
        case 1:
            lerArquivo(arqAlunos)
        case 2:
            cabecalho('Cadastrar novo Aluno')
            nome = str(input('Nome do aluno: ')).strip().capitalize()
            idade = lerInt('Idade do aluno: ')
            turma = str(input('Turma do aluno: ')).strip().upper()
            cadastrarAluno(arqAlunos, nome, idade, turma)
        case 3:
            lerArquivo(arqApresentacoes)
        case 4:
            cabecalho('Agendar nova Apresentação')
            tema = str(input('Tema/Conteúdo da Apresentação: ')).strip().capitalize()
            dia = lerInt('Dia: ')
            mes = lerInt('Mês: ')
            cadastrarApresentacao(arqApresentacoes, tema, dia, mes)


        case 5:
            print(linha(42))
            print(f'{vermelho}Obrigado por utilizar o sistema!{limpaCor}')
            break
        case _:
            print(f'{vermelho}Por favor, escolha uma opção válida!{limpaCor}')
