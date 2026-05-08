def union(first_list, second_list):
    list_zip = []
    for item in zip(first_list, second_list):
        list_zip.append(item)
    return list_zip
    
    
# test = union(['Salvador', 'Ubatuba', 'Belo horizonte', 'Rio de janeo', 'Campo formoso'], ['BA', 'SP', 'MG', 'RJ'])
# print(test)

def union_primitive(first_list: list, second_list: list) -> list:
    list_zip = []
    cont = 0

    if len(first_list) > len(second_list):
        for item in first_list:
            if cont == len(second_list):
                break
            else:
                list_zip.append((item, second_list[cont]))
                cont += 1
        return list_zip

    elif len(second_list) > len(first_list):
        for item in second_list:
            if cont == len(first_list):
                break
            else:
                list_zip.append((item, first_list[cont]))
                cont += 1
        return list_zip
    
    else:
        for item in first_list:
            list_zip.append((item, second_list[cont]))
            cont += 1
        return list_zip
        

# test = union_primitive(['Salvador', 'Ubatuba', 'Belo horizonte'], ['BA', 'SP', 'MG'])
# print(test)

def uniao(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    lista_zippada = [
        (lista1[item], lista2[item]) 
        for item in range(intervalo)
    ]
    # for item in range(intervalo):
    #     lista_zippada.append((lista1[item], lista2[item]))
    
    return lista_zippada

teste = uniao(['Salvador', 'Ubatuba', 'Belo horizonte'], ['BA', 'SP', 'MG', 'RJ'])
print(teste)