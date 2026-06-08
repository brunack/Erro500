import csv
from crip import *

inventario = {
    "01": {'ID': "01", 'nome': "Teclado",'marca': "Red Dragon", 'quantidade': 10, 'preco': 150.00, 'importado': False},
    "02": {'ID': "02", 'nome': "Mouse", 'marca': "Red Dragon", 'quantidade': 20, 'preco':  89.90, 'importado': True },
}

def salvar_csv(caminho: str = inventario) -> None:
    "Salva o catálogo atual no arquivo CSV com separador ';'."
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["ID","Marca", "Nome", "Quantidade", "Preço", "Importado"])

# ─────────────────────────────────────────
#  CADASTRO - PoDRuto
# ─────────────────────────────────────────
def add_produto(inventario):
    print('\n[ PRODUTO ]')
    try:
        id_produto = int(input('ID do produto: '))
        if id_produto in inventario:
            print('ERRO!\n Já existe um produto com este ID')
            return

        nome = input('Nome do produto: ')
        marca = input('Marca do produto: ')
        quantidade = input('Quantidade do produto: ')
        preco = float(input('Preço do produto: '))
        importado = bool(input('Importado? [S/N] ')).upper()
        if importado == 'N':
            importado = False
        else:
            importado = True
        inventario[id_produto] = {'ID': id_produto,
                                  'nome': nome,
                                  'marca': marca,
                                  'quantidade': quantidade,
                                  'preco': preco,
                                  'importado': importado
                                  }
        print('Podruto adicionado com sucesso!')

    except ValueError:
        print('ERROR, Entrada invalida!!!, ID e quantidade precisam ser numeros inteiros, e o preço deve ser numero, '
              'e o importado deve ser "S" OU "N"')

def remov_produto(inventario):
    print('\n[REMOVEDO DI PRODUTO ]')
    try:
        id_produto = int(input('Digite o ID do produto a ser removido: '))
        if id_produto in inventario:
            inventario.pop(id_produto)
            print(f'Podruto {inventario[id_produto]['nome']} removido com sucesso!')
        else:
            print('ZIFUDEU TEM Não')
    except ValueError:
        print('VALOR INVALIDO')

def atualizar_produto(inventario, id_produto, nome, marca, quantidade, preco, importado):
    inventario[id_produto]['nome']       = nome
    inventario[id_produto]['marca']      = marca
    inventario[id_produto]['quantidade'] = quantidade
    inventario[id_produto]['preco']      = preco
    inventario[id_produto]['importado']  = importado
    print(f"Produto '{id_produto}' atualizado com sucesso.")

def solicitar_atualizacao(inventario):
    """Solicita ao usuário o ID do produto e os novos valores."""

    id_produto = input("Digite o ID do produto que deseja atualizar: ")

    if id_produto not in inventario:
        print(f"Produto '{id_produto}' não encontrado no inventário.")
        return

    print(f"\nDados atuais: {inventario[id_produto]}")
    print("Informe os novos valores:\n")

    nome       = input("Novo nome: ")
    marca      = input("Nova marca: ")
    quantidade = int(input("Nova quantidade: "))
    preco      = float(input("Novo preço: "))
    importado  = input("Importado? (s/n): ").strip().lower() == 's'

    atualizar_produto(inventario, id_produto, nome, marca, quantidade, preco, importado)

def valor_total_estoque(quantidade: int, preco: float) -> float:
    total: float = float(quantidade) * preco
    return total

valor_total_estoque()


def login():
    print('\n[ LOGIN ]')

    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:
        print('[ ! ] Nenhum usuário cadastrado ainda.')
        return False

    tentativa_usuario = input('Usuário: ')
    tentativa_senha   = input('Senha  : ')

    usuarios = carregar_usuarios()

    hash_usuario = hash1(cifra_cezar_plus(tentativa_usuario))
    hash_senha   = hash1(cifra_cezar_plus(tentativa_senha))

    if hash_usuario in usuarios and usuarios[hash_usuario] == hash_senha:
        print(f'\n[ ✓ ] Bem-vindo, {tentativa_usuario}!')
        return True
    else:
        print('\n[ ✗ ] Usuário ou senha incorretos.')
        return False

# ─────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────

def menu():
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
            login()
        elif opcao == '0':
            print('Até mais!')
            break
        else:
            print('[ ! ] Opção inválida.')
            
menu()
#MENU PARA CADASTRO - REMOÇÃO - ALTERAÇÃO.
def cadastro_crude():
    while True:
        print('ESCOLHA UMA DA OPÇÕES ABAIXO!')
        print('[1]PARA ADICIONAR PRODUTO')
        print('[2]PARA ATUALIZAR PRODUTO')
        print('[3]PARA REMOVER PRODUTO')
        print('[4]VALOR TORAL DO ESTOQUE')
        print('[5]SAIR E SALVAR')

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            add_produto()
        elif opcao == '2':
            solicitar_atualizacao()
        elif opcao == '3':
            remov_produto()
        elif opcao == '4':
            valor_total_estoque()
        elif opcao == '5':
            salvar_produto()
        elif opcao == '6':
            print('Até mais!')

            break
        else:
            print('[ ! ] Opção inválida.')

cadastro_crude()