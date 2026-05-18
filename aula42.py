import time


def exigir_login(func):
    print('Executando função painel')
    tempo_inicial = time.time()
    def wrapper(*args, **kwargs):
        if not args and not kwargs:
            return 'Acesso negado' 
        return func(*args, **kwargs)
    tempo_final = time.time()
    print(f'Função executada em {tempo_final - tempo_inicial:.6f}s')
    return wrapper

@exigir_login
def painel(usuario=False):
    return f'Bem-vindo {usuario}!'

print(painel('Enzo'))