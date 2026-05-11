import requests
from time import time, sleep 

def monitoring_time(func): 
    def wrapper(*args, **kwargs):
        start_time = time()
        print('Iniciando execução...')
        sleep(2)
        save_func = func(*args, **kwargs)
        end_time = time()
        duration = end_time - start_time
        print(f'Execução finalizada. Tempo de execução: {duration:.2f}')
        return save_func

    return wrapper


@monitoring_time
def my_sum(x: float, y: float) -> float:
    return x + y


test = my_sum(19, 4)
print(test)
