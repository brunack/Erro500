from random import randint


def lista(qtd, vmin=10, vmax=99):
    L = []
    for _ in range(qtd):
        L.append(randint(vmin, vmax))
    return L


def ordenada(L):
    """
    Função que compara os itens da lista para saber se eles estao ordenados.
    """
    i = 0

    while i < len(L) - 1:
        if L[i] > L[i + 1]:
            return False
        i += 1
    return True


def troca(L, i, j):
    """
    Troca posiçoes da lista L nos indices i e j.
    """
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def empurra_maximo(L, n):
    """
    Desloca o item maximo da lista L que tem n intens para o final.
    """
    i = 0
    while i < n - 1:
        if L[i] > L[i + 1]:
            troca(L, i, i + 1)
        i += 1


def empurra_minimo(L, n):
    """
    Desloca o item maximo da lista L que tem n intens para o final.
    """
    i = 0
    while i < n - 1:
        if L[i] < L[i + 1]:
            troca(L, i, i + 1)
        i += 1


def bubble_sort(L, crescente=True):
    """
    ordena a ordem da lista L de forma crescente ou decrescente.
    """

    if crescente:
        empurra = empurra_maximo
    else:
        empurra = empurra_minimo

    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1


# ------------------------------------
def selection_min(L, n):
    maior = 0
    for i in range(1, n):
        if L[i] < L[maior]:
            m = i
        return m


def selection_max(L, n):
    maior = 0
    for i in range(1, n):
        if L[i] > L[maior]:
            m = i
        return m


def selection_sort(L):
    if crescente:
        selection = selection_min
    else:
        selection = selection_max

    n = len(L)
    while n > 1:
        n = selection(L, n)
        troca(L, m, n - 1)
        n -= 1


# --------------

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

# ------------------------------------

def seleciona_maximo(L, n):
    m = 0
    for i in range(1, n):
        if L[i] > L[m]:
            m = i
    return m

def seleciona_minimo(L, n):
    m = 0
    for i in range(1, n):
        if L[i] < L[m]:
            m = i
    return m

def selection_sort(L, crescente=True):
    if crescente:
        seleciona = seleciona_maximo
    else:
        seleciona = seleciona_minimo

    n = len(L)
    while n > 1:
        m = seleciona(L, n)
        troca(L, m, n-1)
        n -= 1

# ---------------------------------

def insere(x, L, n):
    u = n-1
    while u >= 0 and x < L[u]:
        L[u+1] = L[u]
        u -= 1
    L[u+1] = x

def insertion_sort(L):
    n = len(L)-1 # parte não ordenada
    u = 0
    while n > 0:
        insere(L[u+1], L, u+1)
        u += 1
        n -= 1
