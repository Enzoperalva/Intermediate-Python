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
        

def union(first_list: list, second_list: list) -> list:
    interval_max = min(len(first_list), len(second_list))
    list_zip = [
        (first_list[item], second_list[item]) 
        for item in range(interval_max)
    ]
    
    return list_zip

test = union(['Salvador', 'Ubatuba', 'Belo horizonte'], ['BA', 'SP', 'MG', 'RJ'])
print(test)