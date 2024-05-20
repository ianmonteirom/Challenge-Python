# Importando as funções e variáveis criadas no arquivo init.py para o arquivo .py principal

from registros import *

# Caso os arquivos necessários para registrar os dados não existam, cria automaticamente
if not existeArquivo(arqAlunos):
    criarArquivo(arqAlunos)
if not existeArquivo(arqApresentacoes):
    criarArquivo(arqApresentacoes)

# Função com o conteúdo do programa principal
lerEscolha()
