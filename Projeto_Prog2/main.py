import time
import csv
from LockCipher import *
from CRUDE import *


personagens = {id:['Nome','Habilidade','PR','SpecialAtk','Lendario']}

def salvar_csv(caminho: str = personagens) -> None:
    """Salva o catálogo atual no arquivo CSV com separador ';'."""
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["ID","Marca", "Nome", "Quantidade", "Preço", "Importado"])

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
def cadastro_crude():
    while True:
        print('ESCOLHA UMA DA OPÇÕES ABAIXO!')
        print('[1]PARA ADICIONAR PERSONAGEM')
        print('[2]PARA ATUALIZAR PERSONAGEM')
        print('[3]PARA REMOVER PERSONAGEM')
        print('[4]VALOR TOTAL DE PERSONAGEM(S)')
        print('[5]SAIR E SALVAR')

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
            salvar_personagem(personagens)

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
                cadastro_crude()
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