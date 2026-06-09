import time

def listar_detalhada(personagens):
    print(f"{'ID':<5} | {'Nome':<15} | {'PR':<8} | {'Atk':<6} | {'Tipo':<8}")
    print("-" * 50)

    for id_p, atributos in personagens.items():
        # Desempacotando a lista
        nome = atributos[0]
        pr = atributos[2]
        atk = atributos[3]
        lendaria = atributos[4]
        lendaria2 = 'Lendaria' if lendaria == True else 'Comum'

        print(f"{id_p:<8} | {nome:<15} | {pr:<8.1f} | {atk:<6} | {lendaria2:<8} ")
        time.sleep(2)

    print('\n\n')
# -----------------------------------------------------------------------
# MERGE_SORT
# -----------------------------------------------------------------
def mescla(L, i, m, f):
    T = []
    k, j = i, m+1
    while k <= m and j <= f:
        if L[k] < L[j]:
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

def merge_sort(L, i, f):
    if i == f: return
    m = (i + f) // 2
    merge_sort(L, i, m)
    merge_sort(L, m+1, f)
    mescla(L, i, m, f)

def msort(L): # wrapper
    merge_sort(L, 0, len(L)-1)

# ------------------------------------------------------------------
# Burble_sort ------------------------------------------------------

def troca(L, i, j):
    """
    Trocará de lugar os itens de L nos
    índice i e j de lugar.
    """
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def empurra_maximo(L, n):
    """
    Desloca o item máximo da lista L que tem
    n itens para o final.
    """
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            troca(L, i, i+1)
        i += 1

def empurra_minimo(L, n):
    """
    Desloca o item máximo da lista L que tem
    n itens para o final.
    """
    i = 0
    while i < n-1:
        if L[i] < L[i+1]:
            troca(L, i, i+1)
        i += 1

def bubble_sort(L, crescente=True):
    """
    Ordena a lista L em ordem crescente.
    """
    if crescente:
        empurra = empurra_maximo
    else:
        empurra = empurra_minimo

    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1

# -------------------------


def busca_binario(n):
    if n < 2:
        print(n, end='')
    else:
        busca_binario(n // 2)
        print(n % 2, end='')

def binario2(n):
    if n < 2:
        return str(n)
    else:
        bin_metade = binario2(n // 2)
        return bin_metade + str(n % 2)

def busca_linear(personagens):
    nome = input('Digite o nome: ')
    print(f"{'ID':<5} | {'Nome':<15} | {'PR':<8} | {'Atk':<6} | {'Tipo':<8}")
    print("-" * 50)

    for id_p, atributos in personagens.items():
        # Desempacotando a lista
        nome_galeria = atributos[0]
        pr = atributos[2]
        atk = atributos[3]
        lendaria = atributos[4]
        nome3 = str(nome_galeria).lower()
        lendaria2 = 'Lendaria' if lendaria == True else 'Comum'
        if nome3 == nome.lower() :
            print(f"{id_p:<8} | {nome_galeria:<15} | {pr:<8.1f} | {atk:<6} | {lendaria2:<8} ")    

    print('\n\n')
    time.sleep(2)

    