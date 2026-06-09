def salvar_personagem(listinhacsv, personagems):
    """Salva o dicionario em CSV, usando a função de cifra em todos os campos """
    try:
        with open(listinhacsv, 'w', newline='', encoding='utf-8') as f:
        #Estamos usando 'utf-8' para não ocorrer problema de interpretação
        # e o 'as f' para facilitar a manipulação do arquivo
            for id_personagem, atributo in personagems.items():
                csv_cifrada = []
                #cifrar o ID de personagem
                csv_cifrada.append(cifra_cezar_plus(str(id_personagem)))
                #cifrar os atributos dentro do id
                for campo in atributo:
                    csv_cifrada.append(cifra_cezar_plus(str(campo)))

                juntas = ";".join(csv_cifrada)
                f.write(juntas + '\n')
        print('Personagem(s) salvo com sucesso!')
    except Exception:
        print('Erro ao salvar personagem(s).!')