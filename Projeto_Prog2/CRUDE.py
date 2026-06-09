# ─────────────────────────────────────────
# CADASTRO, REMOÇÃO, ALTERAÇÃO DOS PRODUTOS
# ─────────────────────────────────────────

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
        lendario = bool(input('Lendario? [S/N] ')).upper()
        if lendario == 'N':
            lendario = False
        else:
            lendario = True
        inventario[id_personagem] = {'nome': nome,
                                  'Habilidade': habilidade,
                                  'PR': pr,
                                  'SpecialAtk': special,
                                  'Lendario': lendario
                                  }
        print('Personagem adicionado com sucesso!')

    except ValueError:
        print('ERROR, Entrada invalida!!!, ID e SpecialAtk precisam ser numeros inteiros, o PR precisa ser um numero '
              'e o Lendario deve ser "S" OU "N"')

def remov_personagem(inventario):
    print('\n[REMOVER PERSONAGEM ]')
    try:
        id_produto = int(input('Digite o ID do personagem a ser removido: '))
        if id_produto in inventario:
            inventario.pop(id_produto)
            print(f'personagem {inventario[id_produto]['nome']} removido com sucesso!')
        else:
            print('Personagem não encontrado!')
    except ValueError:
        print('VALOR INVALIDO')

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

def valor_total_personagem(valor):
    """Retorna o número total de personagens da galeria."""
    quantidade = len(valor)
    print(f"\n[i] Quantidade total de personagens: {quantidade}")
