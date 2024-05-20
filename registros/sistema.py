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
continuar = True
while continuar:
    menu(opcoes)
    opcao = lerInt(f'{verde}Sua escolha: {limpaCor}')
    lerEscolha(opcao, continuar)
