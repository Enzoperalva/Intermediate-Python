# My solution
def sum_list(first_list: list, second_list: list) -> list:
    interval_max = min(len(first_list), len(second_list))
    list_finally = [
        first_list[item] + second_list[item] 
        for item in range(interval_max)
    ]

    return list_finally
        

test = sum_list([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# print(test)

# My solution for other programming language

def adding_list(first_list: list, second_list: list) -> list:
    list_finally = []
    cont = 0

    if len(first_list) >= len(second_list):
        for item in second_list:
            list_finally.append(item + first_list[cont])
            cont += 1

    elif len(first_list) < len(second_list):
        for item in first_list:
            list_finally.append(item + second_list[cont])
            cont += 1

    return list_finally

test_2 = adding_list([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# print(test_2)

# Solution prof
list_a = [1, 2, 3, 4, 5, 6]
list_b = [1, 2, 3, 4]
list_sum = [
    x + y
    for x, y in zip(list_a, list_b)
]
print(list_sum)