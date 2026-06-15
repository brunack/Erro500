# ─────────────────────────────────────────
# FUNÇÕES DE CRIPTOGRAFIA E AUTENTICAÇÃO
# Objetivo: Gerenciar o cadastro e login dos usuários,
# além de proteger os dados utilizando criptografia
# e salvar/carregar informações em arquivos.
# ─────────────────────────────────────────

# Biblioteca responsável pela geração do algoritmo SHA-256
import hashlib

# Biblioteca utilizada para verificar a existência dos arquivos
import os

# Biblioteca utilizada para controlar pequenas pausas no sistema
import time

# Biblioteca utilizada para manipular arquivos CSV
import csv

# Importa as funções do módulo de busca e ordenação
from busca_ordenacao import *


# ─────────────────────────────────────────
# FUNÇÕES DE CRIPTOGRAFIA
# Objetivo: Proteger os dados antes de armazená-los.
# ─────────────────────────────────────────


# FUNÇÃO: Gerar hash SHA-256
# Objetivo: Transformar um texto em uma sequência criptografada irreversível.

def hash1(l):

    """
    Entrada:
    - l: texto que será criptografado.
    """

    # Aplica a criptografia SHA-256
    criptografado = hashlib.sha256(l.encode()).hexdigest()

    """
    Saída:
    Retorna o valor criptografado.
    """

    return criptografado


# FUNÇÃO: Aplicar a Cifra de César personalizada
# Objetivo: Deslocar cada caractere em 60 posições.

def cifra_cezar_plus(c):

    """
    Entrada:
    - c: texto original.
    """

    # Converte o texto em uma lista para permitir alterações
    cifra = list(c)

    # Percorre cada caractere da lista
    for _ in range(len(c)):

        atual = cifra[_]

        # Soma 60 posições ao código ASCII do caractere
        nova = chr(ord(atual) + 60)

        # Substitui o caractere original
        cifra[_] = nova

    """
    Saída:
    Retorna o texto criptografado.
    """

    return ''.join(cifra)


# FUNÇÃO: Reverter a Cifra de César personalizada
# Objetivo: Restaurar o texto original.

def cifra_cezar_reduce(c):

    """
    Entrada:
    - c: texto criptografado.
    """

    cifra = list(c)

    # Percorre todos os caracteres
    for _ in range(len(c)):

        atual = cifra[_]

        # Subtrai 60 posições do código ASCII
        nova = chr(ord(atual) - 60)

        cifra[_] = nova

    """
    Saída:
    Retorna o texto descriptografado.
    """

    return ''.join(cifra)


# ─────────────────────────────────────────
# LEITURA DO ARQUIVO DE LOGIN
# Objetivo: Armazenar e recuperar os dados dos usuários.
# ─────────────────────────────────────────

NOME_ARQUIVO = 'login.txt'


# FUNÇÃO: Carregar usuários cadastrados
# Objetivo: Ler o arquivo e montar um dicionário com os dados.

def carregar_usuarios():

    """
    Saída:
    Retorna um dicionário no formato:
    {usuario_hash: senha_hash}
    """

    usuarios = {}

    # Verifica se o arquivo existe ou está vazio
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:

        return usuarios

    # Abre o arquivo para leitura
    with open(NOME_ARQUIVO, 'r') as arquivo:

        # Percorre cada linha do arquivo
        for linha in arquivo.read().splitlines():

            # Verifica se a linha possui o separador
            if ':' in linha:

                usuario_hash, senha_hash = linha.split(':', 1)

                usuarios[usuario_hash] = senha_hash

    return usuarios


# FUNÇÃO: Salvar um novo usuário
# Objetivo: Adicionar um usuário e sua senha criptografados.

def salvar_usuario(usuario_hash, senha_hash):

    """
    Entrada:
    - usuario_hash: nome do usuário criptografado.
    - senha_hash: senha criptografada.
    """

    with open(NOME_ARQUIVO, 'a') as arquivo:

        arquivo.write(usuario_hash + ':' + senha_hash + '\n')


# ─────────────────────────────────────────
# CADASTRO
# Objetivo: Registrar um novo usuário no sistema.
# ─────────────────────────────────────────


def cadastrar():

    print('\n[ CADASTRO ]')

    # Solicita os dados do usuário
    novo_usuario = input('Nome do usuário: ')

    nova_senha = input('Senha          : ')

    # Carrega todos os usuários cadastrados
    usuarios = carregar_usuarios()

    """
    Processamento:
    Primeiro aplica a Cifra de César.
    Em seguida aplica o SHA-256.
    """

    usuario_hash = hash1(cifra_cezar_plus(novo_usuario))

    # Verifica se o usuário já existe
    if usuario_hash in usuarios:

        print('[ ! ] Esse usuário já existe.')

        return

    senha_hash = hash1(cifra_cezar_plus(nova_senha))

    # Salva o novo usuário
    salvar_usuario(usuario_hash, senha_hash)

    print(f'[ ✓ ] Usuário "{novo_usuario}" cadastrado com sucesso!')


# ─────────────────────────────────────────
# LOGIN
# Objetivo: Validar as credenciais informadas pelo usuário.
# ─────────────────────────────────────────

def login():

    """
    Objetivo:
    Criptografar o login e a senha digitados
    para compará-los com os dados armazenados.
    """

    print('\n[ LOGIN ]')

    # Verifica se existe algum usuário cadastrado
    if not os.path.exists(NOME_ARQUIVO) or os.path.getsize(NOME_ARQUIVO) == 0:

        print('[ ! ] Nenhum usuário cadastrado ainda.')

        return False

    # Solicita as credenciais
    tentativa_usuario = input('Usuário: ')

    tentativa_senha = input('Senha  : ')

    # Carrega os usuários salvos
    usuarios = carregar_usuarios()

    # Criptografa os dados informados
    hash_usuario = hash1(cifra_cezar_plus(tentativa_usuario))

    hash_senha = hash1(cifra_cezar_plus(tentativa_senha))

    # Verifica se os dados correspondem aos cadastrados
    if hash_usuario in usuarios and usuarios[hash_usuario] == hash_senha:

        print(f'\n[ ✓ ] Bem-vindo, {tentativa_usuario}!')

        return True

    else:

        print('\n[ ✗ ] Usuário ou senha incorretos.')

        return False


# ─────────────────────────────────────────
# SALVAR PERSONAGENS
# Objetivo: Armazenar os personagens em um arquivo CSV.
# ─────────────────────────────────────────

def salvar_personagem(listinhacsv, personagems):

    """
    Entrada:
    - listinhacsv: nome do arquivo CSV.
    - personagems: dicionário contendo os personagens.
    """

    try:

        with open(listinhacsv, 'w', newline='', encoding='utf-8') as f:

            # Cria o objeto responsável pela escrita no CSV
            writer = csv.writer(f, delimiter=';')

            # Percorre todos os personagens
            for id_personagem, atributo in personagems.items():

                csv_cifrada = []

                # Criptografa o ID
                csv_cifrada.append(
                    cifra_cezar_plus(str(id_personagem))
                )

                # Criptografa todos os atributos
                for campo in atributo:

                    csv_cifrada.append(
                        cifra_cezar_plus(str(campo))
                    )

                # Escreve a linha no arquivo
                writer.writerow(csv_cifrada)

        print('Personagem(s) salvo com sucesso!')

    except Exception:

        print('Erro ao salvar personagem(s).!')


# ─────────────────────────────────────────
# CARREGAR PERSONAGENS
# Objetivo: Ler o arquivo CSV e restaurar os dados.
# ─────────────────────────────────────────

def carregar_personagems(listacsv):

    """
    Entrada:
    - listacsv: nome do arquivo CSV.
    """

    personagens = {}

    try:

        with open(listacsv, 'r', encoding='utf-8') as f:

            # Percorre cada linha do arquivo
            for campo in f:

                campo = campo.strip()

                # Ignora linhas vazias
                if not campo:

                    continue

                # Separa os campos da linha
                csv_cifrada = campo.split(';')

                csv_decodificado = []

                # Descriptografa cada informação
                for i in csv_cifrada:

                    resultado = cifra_cezar_reduce(i)

                    csv_decodificado.append(resultado)

                # Converte os dados para seus tipos originais
                id_personagem = int(csv_decodificado[0])

                nome = csv_decodificado[1]

                habilidade = csv_decodificado[2]

                pr = float(csv_decodificado[3])

                special = int(csv_decodificado[4])

                """
                Processamento:
                Se o texto for "True",
                o personagem será considerado lendário.
                """

                lendario = csv_decodificado[5] == "True"

                # Adiciona o personagem ao dicionário
                personagens[id_personagem] = [
                    nome,
                    habilidade,
                    pr,
                    special,
                    lendario
                ]

            print('Personagem(s) carregados com sucesso!')

            time.sleep(1)

            return personagens

    except FileNotFoundError:

        """
        Tratamento de erro:
        Executado caso o arquivo ainda não exista.
        """

        print('Arquivo de personagens não encontrado, Iniciando criaçao de arquivo.')

        time.sleep(1)

        return {}

    except Exception as e:

        """
        Tratamento de erro:
        Captura qualquer falha inesperada.
        """

        print(f'Falha no processo de carregamento de personagem: {e}')

        time.sleep(1)

        return {}
