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

        print(f"{id_p:<5} | {nome:<15} | {pr:<8.1f} | {atk:<6} | {lendaria2:<8}")
        time.sleep(2)