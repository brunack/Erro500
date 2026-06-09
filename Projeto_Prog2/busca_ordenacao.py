import time
import unicodedata

import unicodedata

#REMOVER ACENTOS.
def remover_acentos(texto):
    """Remove acentos e caracteres especiais de uma string."""
    # O NFKD separa a letra do acento (ex: 'é' vira 'e' + '´')
    # O encode('ASCII', 'ignore') joga fora tudo que não for letra comum (o '´')
    # O decode('utf-8') transforma de volta em texto legível
    return unicodedata.normalize('NFKD', str(texto)).encode('ASCII', 'ignore').decode('utf-8')

# BUSCA
def listar_detalhada(personagens):
    print(f"\n{'ID':<8} | {'Nome':<15} | {'PR':<8} | {'Atk':<6} | {'Tipo':<8} | {'Habilidade especial':<25}")
    print("-" * 50)

    for id_p, atributos in personagens.items():
        # Desempacotando a lista
        nome = atributos[0]
        pr = atributos[2]
        atk = atributos[3]
        lendaria = atributos[4]
        lendaria2 = 'Lendaria' if lendaria == True else 'Comum'
        habilidade = atributos[1]

        print(f"{id_p:<8} | {nome:<15} | {pr:<8.1f} | {atk:<6} | {lendaria2:<8} | {habilidade:<25} ")

    print('\n')
    time.sleep(2)

def menu_busca_personagem(personagens):
    print('\n[ BUSCA DE PERSONAGEM ]')
    nome_alvo = input('Digite o nome do personagem que deseja buscar: ')

    print("\nEscolha o método de busca:")
    print("[1] Busca Linear")
    print("[2] Busca Binária")
    escolha = input("Opção: ")

    if escolha == '1':
        print("\nIniciando Busca Linear...")
        time.sleep(1)
        # Chama a sua busca linear normal
        resultado = busca_linear(personagens, nome_alvo)

    elif escolha == '2':
        # ────────────────────────────────────────────────
        # ────────────────────────────────────────────────
        print("\nIniciando Busca Binaria...")
        time.sleep(1)
        lista_pronta = ordenar_automatico(personagens)
        resultado = busca_binaria(lista_pronta, nome_alvo)

        if resultado:
            id_p = resultado[0]
            dados = resultado[1]
            print(f"\nPersonagem Encontrado!")
            print(f"ID: {id_p} | Nome: {dados[0]} | Habilidade: {dados[1]} | PR: {dados[2]} | Atk: {dados[3]}")
            time.sleep(1.5)
        else:
            print("\nPersonagem não encontrado.")
            time.sleep(1.5)

# ──────────────────────────────────────────────────────────────────
# ORDENAÇÃO: BUBBLE SORT / MERGE SORT
# ──────────────────────────────────────────────────────────────────
def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def empurra_maximo_personagem(L, n):
    i = 0
    while i < n - 1:
        # L[i][1][0] acessa a lista de atributos [1] e pega o nome [0]
        if L[i][1][0].lower() > L[i + 1][1][0].lower():
            troca(L, i, i + 1)
        i += 1


def bubble_sort_personagens(L):
    n = len(L)
    while n > 1:
        empurra_maximo_personagem(L, n)
        n -= 1
    return L



def mescla_personagens(L, i, m, f):
    '''Adaptaçao para uso com nomes.'''
    T = []
    k, j = i, m + 1
    while k <= m and j <= f:
        # Compara pelo nome
        if L[k][1][0].lower() < L[j][1][0].lower():
            T.append(L[k])
            k += 1
        else:
            T.append(L[j])
            j += 1

    while k <= m:
        T.append(L[k])
        k += 1

    while j <= f:
        T.append(L[j])
        j += 1

    for a in range(len(T)):
        L[i] = T[a]
        i += 1


def merge_sort_recursivo(L, i, f):
    if i >= f: return
    m = (i + f) // 2
    merge_sort_recursivo(L, i, m)
    merge_sort_recursivo(L, m + 1, f)
    mescla_personagens(L, i, m, f)


def msort_personagens(L):
    merge_sort_recursivo(L, 0, len(L) - 1)
    return L


# ──────────────────────────────────────────────────────────────────
# 3. GERENCIADOR DE ORDENAÇÃO (Requisito do Professor)
# ──────────────────────────────────────────────────────────────────
def ordenar_automatico(personagens):
    """Transforma o dicionário em lista e escolhe o melhor metodo"""
    lista_personagens = list(personagens.items())

    if len(lista_personagens) <= 100:
        return bubble_sort_personagens(lista_personagens)
    else:
        return msort_personagens(lista_personagens)

# -------------------------
#BUSCA BINARIA

def busca_binaria(lista_ordenada, nome):
    """Procura pelo id cortando a lista pela metade (A lista DEVE estar ordenada)"""
    baixo = 0
    alto = len(lista_ordenada) - 1

    nome_alvo = remover_acentos(nome.lower())

    while baixo <= alto:
        meio = (baixo + alto) // 2
        nome_original = lista_ordenada[meio][1][0]
        nome_meio = remover_acentos(nome_original.lower())

        if nome_meio == nome_alvo:
            return lista_ordenada[meio]
        elif nome_meio < nome_alvo:
            baixo = meio + 1
        else:
            alto = meio - 1

    return None

#BUSCA LINEAR

def busca_linear(personagens, nome):
    """Busca personagem pelo nome diretamente no dicionário."""

    #Limpa o nome alvo
    nome_alvo = remover_acentos(nome.lower())
    encontrou = False

    for id_p, atributos in personagens.items():
        # Desempacotando a lista
        nome_galeria = atributos[0]
        pr = atributos[2]
        atk = atributos[3]
        lendaria = atributos[4]

        # Limpa o nome do banco de dados que sera usado para comparaçao
        nome3 = remover_acentos(str(nome_galeria).lower())

        lendaria2 = 'Lendária' if lendaria else 'Comum'

        # Se os dois nomes limpos forem iguais:
        if nome3 == nome_alvo:
            print(f"\n{'ID':<5} | {'Nome':<15} | {'PR':<8} | {'Atk':<6} | {'Tipo':<8}")
            print("-" * 50)
            print(f"{id_p:<5} | {nome_galeria:<15} | {pr:<8.1f} | {atk:<6} | {lendaria2:<8}")
            encontrou = True

    if not encontrou:
        print(f"Nenhum personagem com o nome '{nome}' foi encontrado.")

    print('\n')
    time.sleep(2)