import hashlib
import os

# ─────────────────────────────────────────
#  CRIPTOGRAFIA
# ─────────────────────────────────────────

def hash1(l):
    criptografado = hashlib.sha256(l.encode()).hexdigest()
    return criptografado

def cifra_cezar_plus(c):
    cifra = list(c)
    for _ in range(len(c)):
        atual = cifra[_]
        nova = chr(ord(atual) + 3)
        cifra[_] = nova
    return ''.join(cifra)

def cifra_cezar_reduce(c):
    cifra = list(c)
    for _ in range(len(c)):
        atual = cifra[_]
        nova = chr(ord(atual) - 3)
        cifra[_] = nova
    return ''.join(cifra)

# ─────────────────────────────────────────
#  ARQUIVO  (formato: usuario_hash:senha_hash)
# ─────────────────────────────────────────

NOME_ARQUIVO = 'login.txt'

def carregar_usuarios():
    """Lê login.txt e retorna dicionário {usuario_hash: senha_hash}."""
    usuarios = {}
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:
        return usuarios

    with open(NOME_ARQUIVO, 'r') as arquivo:
        for linha in arquivo.read().splitlines():
            if ':' in linha:
                usuario_hash, senha_hash = linha.split(':', 1)
                usuarios[usuario_hash] = senha_hash

    return usuarios

def salvar_usuario(usuario_hash, senha_hash):
    """Adiciona um novo par usuario_hash:senha_hash no arquivo."""
    with open(NOME_ARQUIVO, 'a') as arquivo:
        arquivo.write(usuario_hash + ':' + senha_hash + '\n')

# ─────────────────────────────────────────
#  CADASTRO
# ─────────────────────────────────────────

def cadastrar():
    print('\n[ CADASTRO ]')
    novo_usuario = input('Nome do usuário: ')
    nova_senha   = input('Senha          : ')

    # Verifica se usuario já existe
    usuarios = carregar_usuarios()
    usuario_hash = hash1(cifra_cezar_plus(novo_usuario))

    if usuario_hash in usuarios:
        print('[ ! ] Esse usuário já existe.')
        return

    senha_hash = hash1(cifra_cezar_plus(nova_senha))

    salvar_usuario(usuario_hash, senha_hash)
    print(f'[ ✓ ] Usuário "{novo_usuario}" cadastrado com sucesso!')


# ─────────────────────────────────────────
#  CADASTRO - PoDRuto
# ─────────────────────────────────────────
inventario = {}

def add_produto(inventario):
    print('\n[ PRODUTO ]')
    try:
        id_produto = int(input('ID do produto: '))
        if id_produto in inventario:
            print('ERRO!\n Já existe um produto com este ID')
            return

        nome = input('Nome do produto: ')
        quantidade = input('Quantidade do produto: ')
        preco = float(input('Preço do produto: '))
        importado = bool(input('Importado? [S/N] ')).upper()
        if importado == 'N':
            importado = False
        else:
            importado = True
        inventario[id_produto] = {'ID': id_produto,
                                  'nome': nome,
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

def atualizar(inventario):

def busca_inventario(inventario):


# ADICIONANDO PRODUTO AO BANCO DE DADOS CSV

arquivo_csv = 'inventario.csv'


# ─────────────────────────────────────────
#  LOGIN
# ─────────────────────────────────────────

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
