import time
import csv
from LockCipher import *
from CRUDE import *
from busca_ordenacao import *



def baner():
    print(r"""
  _  __ ____  _____ 
 | |/ // __ \|  ___|
 | ' /| |  | | |_   
 | . \| |__| |  _|  
 |_|\_\\____/|_|    

 THE KING OF FATEC
===================
""")
    time.sleep(2.5)
baner()


#MENU PARA CADASTRO - REMOÇÃO - ALTERAÇÃO.
def cadastro_crude(personagens):
    while True:
        print('ESCOLHA UMA DA OPÇÕES ABAIXO!')
        print('[1]PARA ADICIONAR PERSONAGEM')
        print('[2]PARA ATUALIZAR PERSONAGEM')
        print('[3]PARA REMOVER PERSONAGEM')
        print('[4]VALOR TOTAL DE PERSONAGEM(S)')
        print('[5]LISTA DETALHADA DE PERSONAGEM(S)')
        print('[6]BUSCA LINEAR POR NOME')
        print('[0]SAIR E SALVAR')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            add_personagem(personagens)
        elif opcao == '2':
            solicitar_atualizacao(personagens)
        elif opcao == '3':
            remov_personagem(personagens)
        elif opcao == '4':
            valor_total_personagem(personagens)
        elif opcao == '5':
            listar_detalhada(personagens)
        elif opcao == '6':
            busca_linear(personagens)
        elif opcao == '0':
            salvar_personagem('inventario.csv', personagens)
        

            break
        else:
            print('[ ! ] Opção inválida.')

# ─────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────
def main():
    while True:
        print('\n================================')
        print('       SISTEMA DE LOGIN         ')
        print('================================')
        print('[1] Criar novo usuário')
        print('[2] Fazer login')
        print('[0] Sair')

        opcao = input('\nEscolha: ').strip()

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            if login():
                print('Acesso autorizado')
                time.sleep(2)
                personagens = carregar_personagems('inventario.csv')
                cadastro_crude(personagens)
            else:
                print('Usuario ou senha invalidas')
                time.sleep(1)
        elif opcao == '0':
            print('Até mais!')
            break
        else:
            print('[ ! ] Opção inválida.')
            
if __name__ == "__main__":
    main()