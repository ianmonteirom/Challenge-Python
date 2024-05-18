from registroAlunos import *

opcoes = ['Ver Registro de Alunos', 'Cadastrar novo Aluno', 'Sair do Sistema']

if not existeArquivo(arqAlunos):
    criarArquivo(arqAlunos)

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
            cadastrar(arqAlunos, nome, idade, turma)
        case 3:
            print(linha(42))
            print(f'{vermelho}Obrigado por utilizar o sistema!{limpaCor}')
            break
        case _:
            print(f'{vermelho}Por favor, escolha uma opção válida!{limpaCor}')
