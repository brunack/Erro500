# ─────────────────────────────────────────
# CADASTRO, REMOÇÃO, ALTERAÇÃO DOS PRODUTOS
# Objetivo: Gerenciar os personagens do inventário, permitindo
# adicionar, remover, atualizar e consultar a quantidade total.
# ─────────────────────────────────────────

import time


# FUNÇÃO: Adicionar um novo personagem ao inventário
# Objetivo: Solicitar os dados do personagem e armazená-los no inventário.

def add_personagem(inventario):

    print('\n[ PERSONAGEM ]')

    """
    Entrada:
    - inventario: dicionário que armazena todos os personagens cadastrados.
    """

    try:

        # Solicita o ID do personagem
        id_personagem = int(input('ID do personagem: '))

        # Verifica se o ID já está cadastrado
        if id_personagem in inventario:
            print('ERRO!\n Já existe um personagem com este ID')
            return

        # Solicita os dados do personagem
        nome = input('Nome do personagem: ')
        habilidade = input('Habilidade especial: ')
        pr = float(input('Percentual de rendimento: '))
        special = int(input('Special Atk: '))
        resp = input('Lendário? [S/N]: ').strip().upper()

        """
        Processamento:
        Caso o usuário digite "S", o personagem será marcado
        como lendário (True). Qualquer outra resposta será False.
        """
        lendario = True if resp == 'S' else False

        # Armazena os dados no inventário
        inventario[id_personagem] = [nome, habilidade, pr, special, lendario]

        print('Personagem adicionado com sucesso!')

    except ValueError:

        """
        Tratamento de erro:
        Executado caso o usuário digite um valor incompatível.
        """

        print(
            'ERROR, Entrada invalida!!!, ID e SpecialAtk precisam ser numeros inteiros, '
            'o PR precisa ser um numero e o Lendario deve ser "S" OU "N"'
        )

        time.sleep(1.5)


# FUNÇÃO: Remover um personagem do inventário
# Objetivo: Excluir um personagem utilizando seu ID.

def remov_personagem(inventario):

    print('\n[ REMOVER PERSONAGEM ]')

    """
    Entrada:
    - inventario: dicionário contendo os personagens cadastrados.
    """

    try:

        # Solicita o ID do personagem que será removido
        id_produto = int(input('Digite o ID do personagem a ser removido: '))

        # Verifica se o ID existe no inventário
        if id_produto in inventario:

            # Remove o personagem e armazena seus dados temporariamente
            personagem_removido = inventario.pop(id_produto)

            print(f"Personagem '{personagem_removido[0]}' removido com sucesso!")

            time.sleep(1)

        else:

            print('Personagem não encontrado!')

            time.sleep(1)

    except ValueError:

        """
        Tratamento de erro:
        Ocorre quando o usuário digita um valor diferente de número inteiro.
        """

        print('VALOR INVÁLIDO. Digite apenas números inteiros.')

        time.sleep(1)


# FUNÇÃO: Atualizar os dados de um personagem
# Objetivo: Substituir os dados antigos pelos novos dados informados.

def atualizar_personagem(personagens, id_personagem, nome, habilidade, pr, special, lendario):

    """
    Entrada:
    - personagens: dicionário que armazena todos os personagens.
    - id_personagem: identificador do personagem.
    - nome: novo nome.
    - habilidade: nova habilidade especial.
    - pr: novo percentual de rendimento.
    - special: novo valor de ataque especial.
    - lendario: define se o personagem é lendário.
    """

    # Atualiza os dados do personagem
    personagens[id_personagem] = [nome, habilidade, pr, special, lendario]

    print(f"Personagem '{id_personagem}' atualizado com sucesso.")


# FUNÇÃO: Solicitar atualização dos dados
# Objetivo: Pedir ao usuário os novos dados e chamar a função de atualização.

def solicitar_atualizacao(personagens):

    """
    Entrada:
    - personagens: dicionário que contém todos os personagens cadastrados.
    """

    try:

        # Solicita o ID do personagem
        id_personagem = int(input("Digite o ID do personagem que deseja atualizar: "))

    except ValueError:

        """
        Tratamento de erro:
        O ID obrigatoriamente deve ser um número inteiro.
        """

        print('ERROR, o ID deve ser um número inteiro.!!!')

        return

    try:

        # Verifica se o personagem existe
        if id_personagem not in personagens:

            print(f"Personagem '{id_personagem}' não encontrado na galeria.")

            return

        # Exibe os dados atuais do personagem
        print(f"\nDados atuais: {personagens[id_personagem]}")

        print("Informe os novos valores:\n")

        # Solicita os novos dados
        nome = input('Novo nome do personagem: ')

        habilidade = input('Nova habilidade especial: ')

        pr = float(input('Novo percentual de rendimento: '))

        special = int(input('Novo Special Atk: '))

        resp = input('Lendário? [S/N]: ').strip().upper()

        """
        Processamento:
        Converte a resposta do usuário em um valor booleano.
        """

        lendario = True if resp == 'S' else False

        # Chama a função responsável pela atualização
        atualizar_personagem(
            personagens,
            id_personagem,
            nome,
            habilidade,
            pr,
            special,
            lendario
        )

    except Exception as e:

        """
        Tratamento de erro:
        Captura qualquer erro ocorrido durante a atualização.
        """

        print(
            f'ERROR, Entrada invalida!!!, ID e SpecialAtk precisam ser numeros inteiros, '
            f'o PR precisa ser um numero e o Lendario deve ser "S" OU "N": {e}'
        )


# FUNÇÃO: Exibir a quantidade total de personagens
# Objetivo: Informar quantos personagens existem na galeria.

def valor_total_personagem(valor):

    """
    Entrada:
    - valor: dicionário que armazena todos os personagens.
    """

    # Conta a quantidade de personagens cadastrados
    quantidade = len(valor)

    """
    Saída:
    Exibe a quantidade total de personagens cadastrados.
    """

    print(f"\nQuantidade total de personagens: {quantidade}")

    time.sleep(1.5)
