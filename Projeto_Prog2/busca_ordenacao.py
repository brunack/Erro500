# ─────────────────────────────────────────
# BUSCA E ORDENAÇÃO DE PERSONAGENS
# Objetivo: Permitir a listagem, busca e ordenação
# dos personagens utilizando diferentes algoritmos.
# ─────────────────────────────────────────

import time
import unicodedata


# FUNÇÃO: Remover acentos
# Objetivo: Padronizar os textos para evitar erros durante as buscas.

def remover_acentos(texto):

    """
    Entrada:
    - texto: palavra ou frase que será normalizada.
    """

    """
    Processamento:
    - Separa os caracteres dos acentos.
    - Remove os acentos.
    - Retorna somente caracteres simples.
    """

    return unicodedata.normalize(
        'NFKD',
        str(texto)
    ).encode(
        'ASCII',
        'ignore'
    ).decode('utf-8')

# ─────────────────────────────────────────
# LISTAGEM DE PERSONAGENS
# Objetivo: Exibir todos os personagens cadastrados.
# ─────────────────────────────────────────

def listar_detalhada(personagens):
    """
        Objetivo: Exibir no terminal a galeria completa de personagens formatada em tabela.
        Entrada: personagens (dicionário principal).
        Saída: Nenhuma (Apenas impressão visual).
        """

    print(
        f"\n{'ID':<8} | {'Nome':<15} | {'PR':<8} | "
        f"{'Atk':<6} | {'Tipo':<8} | {'Habilidade especial':<25}"
    )

    print("-" * 50)

    # Percorre todos os personagens cadastrados
    for id_p, atributos in personagens.items():

        """
        Processamento:
        Separa cada informação armazenada na lista.
        """

        nome = atributos[0]

        pr = atributos[2]

        atk = atributos[3]

        lendaria = atributos[4]

        habilidade = atributos[1]

        """
        Processamento:
        Converte o valor booleano em um texto.
        """

        lendaria2 = 'Lendaria' if lendaria else 'Comum'

        print(
            f"{id_p:<8} | "
            f"{nome:<15} | "
            f"{pr:<8.1f} | "
            f"{atk:<6} | "
            f"{lendaria2:<8} | "
            f"{habilidade:<25}"
        )

    print('\n')

    time.sleep(2)


# ─────────────────────────────────────────
# MENU DE BUSCA
# Objetivo: Permitir ao usuário escolher o algoritmo de busca.
# ─────────────────────────────────────────

def menu_busca_personagem(personagens):
    """
        Objetivo: Interface interativa para o usuário escolher o método de pesquisa.
        Entrada: personagens (dicionário principal).
        Ação: Solicita o nome, chama o algoritmo escolhido (Linear ou Binário) e exibe o resultado.
        """

    print('\n[ BUSCA DE PERSONAGEM ]')

    # Solicita o nome do personagem
    nome_alvo = input(
        'Digite o nome do personagem que deseja buscar: '
    )

    print("\nEscolha o método de busca:")

    print("[1] Busca Linear")

    print("[2] Busca Binária")

    escolha = input("Opção: ")

    # Busca Linear
    if escolha == '1':

        print("\nIniciando Busca Linear...")

        time.sleep(1)

        resultado = busca_linear(
            personagens,
            nome_alvo
        )

    # Busca Binária
    elif escolha == '2':

        print("\nIniciando Busca Binaria...")

        time.sleep(1)

        """
        Processamento:
        A Busca Binária exige que os dados
        estejam previamente ordenados.
        """

        lista_pronta = ordenar_automatico(
            personagens
        )

        resultado = busca_binaria(
            lista_pronta,
            nome_alvo
        )

        if resultado:

            id_p = resultado[0]

            dados = resultado[1]

            print(f"\nPersonagem Encontrado!")

            print(
                f"ID: {id_p} | "
                f"Nome: {dados[0]} | "
                f"Habilidade: {dados[1]} | "
                f"PR: {dados[2]} | "
                f"Atk: {dados[3]}"
            )

            time.sleep(1.5)

        else:

            print("\nPersonagem não encontrado.")

            time.sleep(1.5)


# ─────────────────────────────────────────
# BUBBLE SORT
# Objetivo: Organizar os personagens por ordem alfabética.
# ─────────────────────────────────────────


# FUNÇÃO: Trocar elementos de posição

def troca(L, i, j):
    """
        Objetivo: Inverter a posição de dois itens dentro de uma lista.
        Entrada: L (lista), i (índice 1), j (índice 2).
        """
    """
    Entrada:
    - L: lista principal.
    - i: primeira posição.
    - j: segunda posição.
    """

    temp = L[i]

    L[i] = L[j]

    L[j] = temp


# FUNÇÃO: Empurrar o maior elemento

def empurra_maximo_personagem(L, n):

    """
    Objetivo:
    Comparar os nomes adjacentes e mover
    os maiores para o final da lista.
    """

    i = 0

    while i < n - 1:

        if L[i][1][0].lower() > L[i + 1][1][0].lower():

            troca(L, i, i + 1)

        i += 1


# FUNÇÃO: Bubble Sort

def bubble_sort_personagens(L):

    """
    Objetivo:
    Ordenar listas pequenas de forma simples.
    """

    n = len(L)

    while n > 1:

        empurra_maximo_personagem(L, n)

        n -= 1

    return L


# ─────────────────────────────────────────
# MERGE SORT
# Objetivo: Organizar listas grandes de forma eficiente.
# ─────────────────────────────────────────


# FUNÇÃO: Mesclar listas ordenadas

def mescla_personagens(L, i, m, f):
    """
        Objetivo: Função auxiliar do Merge Sort. Junta duas metades de uma lista mantendo a ordem alfabética.
        Entrada: L (lista principal), i (início), m (meio), f (fim).
        """
    """
    Entrada:
    - L: lista principal.
    - i: posição inicial.
    - m: posição central.
    - f: posição final.
    """

    T = []

    k, j = i, m + 1

    while k <= m and j <= f:

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

    # Atualiza a lista principal
    for a in range(len(T)):

        L[i] = T[a]

        i += 1


# FUNÇÃO: Divisão recursiva do Merge Sort

def merge_sort_recursivo(L, i, f):

    """
    Objetivo:
    Dividir a lista em partes menores.
    """

    if i >= f:

        return

    m = (i + f) // 2

    merge_sort_recursivo(L, i, m)

    merge_sort_recursivo(L, m + 1, f)

    mescla_personagens(L, i, m, f)


# FUNÇÃO: Inicializar o Merge Sort

def msort_personagens(L):
    """
        Objetivo: Inicializa e executa o algoritmo Merge Sort para listas grandes (> 100 itens).
        Entrada: L (lista de personagens não ordenada).
        Saída: Retorna a lista L ordenada.
        """

    merge_sort_recursivo(
        L,
        0,
        len(L) - 1
    )

    return L


# ─────────────────────────────────────────
# GERENCIADOR DE ORDENAÇÃO
# Objetivo: Escolher automaticamente o melhor algoritmo.
# ─────────────────────────────────────────

def ordenar_automatico(personagens):
    """
        Objetivo: Gerenciar qual algoritmo de ordenação usar baseado no tamanho do banco de dados.
        Entrada: personagens (dicionário principal).
        Saída: Retorna uma lista de tuplas ordenada alfabeticamente.
        """

    """
    Processamento:

    Até 100 personagens:
    - Utiliza Bubble Sort.

    Acima de 100 personagens:
    - Utiliza Merge Sort.
    """

    lista_personagens = list(
        personagens.items()
    )

    if len(lista_personagens) <= 100:

        return bubble_sort_personagens(
            lista_personagens
        )

    else:

        return msort_personagens(
            lista_personagens
        )


# ─────────────────────────────────────────
# BUSCA BINÁRIA
# Objetivo: Encontrar um personagem dividindo
# a lista ordenada pela metade.
# ─────────────────────────────────────────

def busca_binaria(lista_ordenada, nome):
    """
        Objetivo: Encontrar um personagem rapidamente usando divisão e conquista.
        Entrada: lista_ordenada (lista pré-ordenada), nome (string do alvo).
        Saída: Retorna a tupla do personagem se encontrado, ou None se não existir.
        """

    """
    Importante:
    A lista obrigatoriamente precisa
    estar ordenada.
    """

    baixo = 0

    alto = len(lista_ordenada) - 1

    nome_alvo = remover_acentos(
        nome.lower()
    )

    while baixo <= alto:

        meio = (baixo + alto) // 2

        nome_original = lista_ordenada[meio][1][0]

        nome_meio = remover_acentos(
            nome_original.lower()
        )

        if nome_meio == nome_alvo:

            return lista_ordenada[meio]

        elif nome_meio < nome_alvo:

            baixo = meio + 1

        else:

            alto = meio - 1

    return None


# ─────────────────────────────────────────
# BUSCA LINEAR
# Objetivo: Percorrer toda a galeria
# até encontrar o personagem.
# ─────────────────────────────────────────

def busca_linear(personagens, nome):
    """
        Objetivo: Encontrar um personagem vasculhando o dicionário item por item.
        Entrada: personagens (dicionário principal), nome (string do alvo).
        Saída: Nenhuma (Imprime o resultado diretamente na tela).
        """

    nome_alvo = remover_acentos(
        nome.lower()
    )

    encontrou = False

    # Percorre todos os personagens
    for id_p, atributos in personagens.items():

        nome_galeria = atributos[0]

        pr = atributos[2]

        atk = atributos[3]

        lendaria = atributos[4]

        nome3 = remover_acentos(
            str(nome_galeria).lower()
        )

        lendaria2 = (
            'Lendária'
            if lendaria
            else 'Comum'
        )


        # Verifica se os nomes são iguais
        if nome3 == nome_alvo:

            print(
                f"\n{'ID':<5} | "
                f"{'Nome':<15} | "
                f"{'PR':<8} | "
                f"{'Atk':<6} | "
                f"{'Tipo':<8}"
            )

            print("-" * 50)

            print(
                f"{id_p:<5} | "
                f"{nome_galeria:<15} | "
                f"{pr:<8.1f} | "
                f"{atk:<6} | "
                f"{lendaria2:<8}"
            )

            encontrou = True

    if not encontrou:

        print(
            f"Nenhum personagem com o nome "
            f"'{nome}' foi encontrado."
        )

    print('\n')

    time.sleep(2)
