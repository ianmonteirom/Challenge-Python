# Importação da função sleep() para dar um efeito de "processando" no programa
from time import sleep

# Declaração de variáveis de cores no terminal
limpaCor, vermelho, verde, amarelo, azul, azulClaro = ('\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[34m',
                                                       '\033[36m')


# Função que retorna uma linha de acordo com o tamanho desejado
def linha(tam):
    return '--' * tam


# Função que printa um cabeçalho com o texto centralizado, entre duas linhas horizontais
def cabecalho(txt):
    print(linha(42))
    print(txt.center(42 * 2))
    print(linha(42))


# Função que printa o menu de opções do sistema
def menu(opcoes):
    cabecalho('Sistema de Registro para as Escolas')
    for i in range(len(opcoes)):
        print(f'{amarelo}{i + 1} {limpaCor}- {azul}{opcoes[i]}{limpaCor}')


# Função que lê um input de um número inteiro sem dar erro e crashar o programa
def lerInt(txt):
    try:
        n = int(input(txt))
    except:
        print(f'{vermelho}Por favor, digite um número inteiro.{limpaCor}')
    else:
        return n


# Declaração da variável com o nome do arquivo do registro dos alunos, para facilitar na escrita do código
arqAlunos = 'alunos.txt'

# Declaração da variável com o nome do arquivo das apresetanções agendadas, para facilitar na escrita do código
arqApresentacoes = 'apresentacoes.txt'


# Função que checa se um arquivo existe ou não, retornando True se existe ou False caso não
def existeArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{vermelho}Arquivo de registro {nome} não encontrado, criando...{limpaCor}')
        sleep(1.5)
        return False
    else:
        return True


# Função que cria um arquivo
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print(f'{vermelho}Erro! Não foi possível criar o arquivo.{limpaCor}')
    else:
        print(f'{verde}Arquivo de registro {nome} criado com sucesso!{limpaCor}')
        sleep(1.5)
    finally:
        a.close()


# Declaração de uma variável para facilitar na formatação dos dados que aparecerão no console
espaco = ''


# Função que lê o conteúdo de um arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{vermelho}Erro! Não foi possível ler o arquivo.{limpaCor}')
    else:
        if nome == arqAlunos:
            cabecalho('Alunos Registrados no Sistema')
        elif nome == arqApresentacoes:
            cabecalho('Apresentações Agendadas no Sistema')
        for linhas in a:
            dado = linhas.split(';')
            dado[2] = dado[2].replace('\n', '')
            if nome == arqAlunos:
                print(f'Nome: {dado[0]:<15} {espaco:>10}Idade: {dado[1]:>5} {espaco:>10}Turma: {dado[2]:>15}')
            elif nome == arqApresentacoes:
                print(f'Tema: {dado[0]:<50} {espaco:>15}Data: {dado[1]}/{dado[2]}\t')
        sleep(2)
    finally:
        a.close()


# Função que cadastra um novo aluno no sistema
def cadastrarAluno(arquivo, nome='desconhecido', idade=0, turma='desconhecida'):
    try:
        a = open(arqAlunos, 'at')
    except:
        print(f'{vermelho}Não foi possível adicionar o novo registro.{limpaCor}')
    else:
        a.write(f'{nome};{idade};{turma}\n')
        a.close()


# Função que agenda uma nova apresentação no sistema
def cadastrarApresentacao(arquivo, tema='desconhecido', dia=0, mes=0):
    try:
        a = open(arqApresentacoes, 'at')
    except:
        print(f'{vermelho}Não foi possível agendar a nova apresentação.{limpaCor}')
    else:
        a.write(f'{tema};{dia};{mes}\n')
        a.close()
