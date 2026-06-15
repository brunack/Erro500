# ─────────────────────────────────────────
# SISTEMA PRINCIPAL
# Objetivo: Controlar o fluxo de execução do programa,
# integrando login, cadastro, inventário, busca,
# ordenação e gerenciamento dos personagens.
# ─────────────────────────────────────────

# Biblioteca utilizada para controlar pausas no sistema
import time

# Biblioteca para manipulação de arquivos CSV
import csv

# Importa todas as funções do módulo de criptografia e login
from LockCipher import *

# Importa todas as funções do CRUD
from CRUDE import *

# Importa todas as funções de busca e ordenação
from busca_ordenacao import *


# ─────────────────────────────────────────
# BANNER DO SISTEMA
# Objetivo: Exibir a identidade visual do projeto.
# ─────────────────────────────────────────

def baner():

    """
    Objetivo:
    Exibir o nome do sistema ao iniciar o programa.
    """

    print(r"""
  _  __ ____  _____ 
 | |/ // __ \|  ___|
 | ' /| |  | | |_   
 | . \| |__| |  _|  
 |_|\_\\____/|_|    

 THE KING OF FATEC
===================
""")

    # Mantém o banner visível por alguns segundos
    time.sleep(2.5)


# Executa o banner logo no início do programa
baner()


# ─────────────────────────────────────────
# MENU DE GERENCIAMENTO DE PERSONAGENS
# Objetivo: Permitir ao usuário administrar
# todo o inventário de personagens.
# ─────────────────────────────────────────

def cadastro_crude(personagens):

    """
    Entrada:
    - personagens: dicionário que armazena todos
      os personagens cadastrados.
    """

    while True:

        print('\n')

        print('ESCOLHA UMA DA OPÇÕES ABAIXO!')

        print('[1]PARA ADICIONAR PERSONAGEM')

        print('[2]PARA ATUALIZAR PERSONAGEM')

        print('[3]PARA REMOVER PERSONAGEM')

        print('[4]VALOR TOTAL DE PERSONAGEM(S)')

        print('[5]LISTA DETALHADA DE PERSONAGEM(S)')

        print('[6]MENU DE BUSCA')

        print('[0]SAIR E SALVAR')

        # Solicita a opção desejada
        opcao = input('Digite a opção desejada: ')

        # Adicionar personagem
        if opcao == '1':

            add_personagem(personagens)

        # Atualizar personagem
        elif opcao == '2':

            solicitar_atualizacao(personagens)

        # Remover personagem
        elif opcao == '3':

            remov_personagem(personagens)

        # Exibir quantidade total
        elif opcao == '4':

            valor_total_personagem(personagens)

        # Exibir todos os personagens
        elif opcao == '5':

            listar_detalhada(personagens)

        # Abrir menu de busca
        elif opcao == '6':

            menu_busca_personagem(personagens)

        # Salvar e sair
        elif opcao == '0':

            """
            Processamento:
            Antes de encerrar o menu, os dados
            são salvos no arquivo CSV.
            """

            salvar_personagem(
                'inventario.csv',
                personagens
            )

            break

        else:

            print('[ ! ] Opção inválida.')


# ─────────────────────────────────────────
# MENU PRINCIPAL
# Objetivo: Controlar o acesso ao sistema.
# ─────────────────────────────────────────

def main():

    """
    Objetivo:
    Exibir o menu inicial do sistema e
    controlar todo o fluxo de execução.
    """

    while True:

        print('\n================================')

        print('       SISTEMA DE LOGIN         ')

        print('================================')

        print('[1] Criar novo usuário')

        print('[2] Fazer login')

        print('[0] Sair')

        # Solicita a opção do usuário
        opcao = input('\nEscolha: ').strip()

        # Cadastro de usuário
        if opcao == '1':

            cadastrar()

        # Login do usuário
        elif opcao == '2':

            """
            Processamento:
            O acesso só será liberado
            caso o login seja validado.
            """

            if login():

                print('Acesso autorizado')

                time.sleep(2)

                """
                Processamento:
                Carrega todos os personagens
                salvos anteriormente.
                """

                personagens = carregar_personagems(
                    'inventario.csv'
                )

                # Abre o menu de gerenciamento
                cadastro_crude(personagens)

            else:

                print('Usuario ou senha invalidas')

                time.sleep(1)

        # Encerrar o programa
        elif opcao == '0':

            print('Até mais!')

            break

        else:

            print('[ ! ] Opção inválida.')


# ─────────────────────────────────────────
# PONTO DE INÍCIO DO PROGRAMA
# Objetivo: Garantir que a função principal
# seja executada ao iniciar o sistema.
# ─────────────────────────────────────────

if __name__ == "__main__":

    """
    Importante:

    "__name__" é uma variável interna do Python.

    Quando seu valor é "__main__",
    significa que este arquivo foi executado
    diretamente pelo usuário.

    Nesse caso, a função principal será iniciada.
    """

    main()
