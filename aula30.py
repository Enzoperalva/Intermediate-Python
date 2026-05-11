def check(func):
    def wrapper(*args, **kwargs):
        print(f'Nome da função chamada: {func.__name__}')
        print(f'Argumentos posicionais recebidos: {args}')
        print(f'Argumentos nomeados recebidos: {kwargs}')
        resultado = func(*args, **kwargs)
        print(f'Resultado da função: ', resultado)
        return resultado
    return wrapper


@check
def my_sum(x: float, y: float) -> float:
    return x + y

test = my_sum(1, 2)
print(test)