#hashlib - biblioteca para o uso do sha256
import hashlib
#os - biblioteca para verificação de arquivo, serve para evitar erros de arquivos nao encontrados.
import os
import time
import csv
from busca_ordenacao import *

# ─────────────────────────────────────────
#  FUNÇÕES DE CRIPTOGRAFIA
# ─────────────────────────────────────────

def hash1(l):
    criptografado = hashlib.sha256(l.encode()).hexdigest()
    return criptografado

def cifra_cezar_plus(c):
    cifra = list(c)
    for _ in range(len(c)):
        atual = cifra[_]
        nova = chr(ord(atual) + 60)
        cifra[_] = nova
    return ''.join(cifra)

def cifra_cezar_reduce(c):
    cifra = list(c)
    for _ in range(len(c)):
        atual = cifra[_]
        nova = chr(ord(atual) - 60)
        cifra[_] = nova
    return ''.join(cifra)

# ─────────────────────────────────────────
#  LEITURA - TXT
# ─────────────────────────────────────────

NOME_ARQUIVO = 'login.txt'

def carregar_usuarios():
    """Lê login.py e retorna dicionário {usuario_hash: senha_hash}."""
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
#  VAlIDAÇÃO DE USUARIO
# ─────────────────────────────────────────

def login():
    """"Função para descriptografar o login e senha, e validar se estão corretos."""
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


def salvar_personagem(listinhacsv, personagems):
    """Salva o dicionario em CSV usando a biblioteca para proteger os dados."""
    try:
        with open(listinhacsv, 'w', newline='', encoding='utf-8') as f:
            # Substitui o .join() pelo writer
            writer = csv.writer(f, delimiter=';')

            for id_personagem, atributo in personagems.items():
                csv_cifrada = []
                csv_cifrada.append(cifra_cezar_plus(str(id_personagem)))
                for campo in atributo:
                    csv_cifrada.append(cifra_cezar_plus(str(campo)))

                # O writerow escreve a linha inteira e protege o ; automaticamente
                writer.writerow(csv_cifrada)

        print('Personagem(s) salvo com sucesso!')
    except Exception:
        print('Erro ao salvar personagem(s).!')

def carregar_personagems(listacsv):
    """Usado para descriptografar e montar o dicionario corretamente."""
    personagens = {}
    try:
        with open(listacsv, 'r', encoding='utf-8') as f:
            for campo in f:
                campo = campo.strip()
                if not campo:
                    continue

                csv_cifrada = campo.split(';')
                csv_decodificado = []
                for i in csv_cifrada:
                    resultado = cifra_cezar_reduce(i)
                    csv_decodificado.append(resultado)

                id_personagem = int(csv_decodificado[0])
                nome = csv_decodificado[1]
                habilidade = csv_decodificado[2]
                pr = float(csv_decodificado[3])
                special = int(csv_decodificado[4])
                lendario = csv_decodificado[5] == "True"
                #true + true = true ; false + true = false

                personagens[id_personagem] = [nome, habilidade, pr, special, lendario]
            print('Personagem(s) carregados com sucesso!')
            time.sleep(1)
            return personagens
    except FileNotFoundError:
        print('Arquivo de personagens não encontrado, Iniciando criaçao de arquivo.')
        time.sleep(1)
        return {}

    except Exception as e:
        print(f'Falha no processo de carregamento de personagem: {e}')
        time.sleep(1)
        return {}