# ─────────────────────────────────────────
# CADASTRO, REMOÇÃO, ALTERAÇÃO DOS PRODUTOS
# ─────────────────────────────────────────
import time


def add_personagem(inventario):
    print('\n[ PERSONAGEM ]')
    try:
        id_personagem = int(input('ID do personagem: '))
        if id_personagem in inventario:
            print('ERRO!\n Já existe um personagem com este ID')
            return

        nome = input('Nome do personagem: ')
        habilidade = input('Habilidade especial: ')
        pr = float(input('Percentual de rendimento: '))
        special = int(input('Special Atk: '))
        resp = input('Lendário? [S/N]: ').strip().upper()
        lendario = True if resp == 'S' else False

        inventario[id_personagem] = [nome, habilidade, pr, special, lendario]

        print('Personagem adicionado com sucesso!')

    except ValueError:
        print('ERROR, Entrada invalida!!!, ID e SpecialAtk precisam ser numeros inteiros, o PR precisa ser um numero '
              'e o Lendario deve ser "S" OU "N"')
        time.sleep(1.5)


def remov_personagem(inventario):
    print('\n[ REMOVER PERSONAGEM ]')
    try:
        id_produto = int(input('Digite o ID do personagem a ser removido: '))
        if id_produto in inventario:
            personagem_removido = inventario.pop(id_produto)

            print(f"Personagem '{personagem_removido[0]}' removido com sucesso!")
            time.sleep(1)
        else:
            print('Personagem não encontrado!')
            time.sleep(1)
    except ValueError:
        print('VALOR INVÁLIDO. Digite apenas números inteiros.')
        time.sleep(1)

def atualizar_personagem(personagens, id_personagem, nome, habilidade, pr, special, lendario):
    personagens[id_personagem] = [nome, habilidade, pr, special, lendario]
    print(f"Personagem '{id_personagem}' atualizado com sucesso.")

def solicitar_atualizacao(personagens):
    """Solicita ao usuário o ID do personagem e os novos valores."""
    try:
        id_personagem = int(input("Digite o ID do personagem que deseja atualizar: "))
    except ValueError:
        print('ERROR, o ID deve ser um número inteiro.!!!')
        return
    try:
        if id_personagem not in personagens:
            print(f"Personagem '{id_personagem}' não encontrado na galeria.")
            return

        print(f"\nDados atuais: {personagens[id_personagem]}")
        print("Informe os novos valores:\n")

        nome = input('Novo nome do personagem: ')
        habilidade = input('Nova habilidade especial: ')
        pr = float(input('Novo percentual de rendimento: '))
        special = int(input('Novo Special Atk: '))
        resp = input('Lendário? [S/N]: ').strip().upper()
        lendario = True if resp == 'S' else False

        atualizar_personagem(personagens, id_personagem, nome, habilidade, pr, special, lendario)
    except Exception as e:
        print(f'ERROR, Entrada invalida!!!, ID e SpecialAtk precisam ser numeros inteiros, o PR precisa ser um numero '
              f'e o Lendario deve ser "S" OU "N": {e}')

def valor_total_personagem(valor):
    """Retorna o número total de personagens da galeria."""
    quantidade = len(valor)
    print(f"\nQuantidade total de personagens: {quantidade}")
    time.sleep(1.5)

