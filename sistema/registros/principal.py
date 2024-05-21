# Importando as funções e variáveis criadas no arquivo init.py para o arquivo .py principal

from registros import *

# Função para caso os arquivos necessários para registrar os dados não existam, cria automaticamente
validarArquivos(arqAlunos, arqApresentacoes)

# Função com o conteúdo do programa principal
lerEscolha()
