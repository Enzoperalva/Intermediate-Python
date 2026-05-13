from functools import reduce

sales = [
    {'product': 'Notebook', 'category': 'tech', 'price': 3000},
    {'product': 'Mouse', 'category': 'tech', 'price': 100},
    {'product': 'Shirt', 'category': 'clothes', 'price': 80},
    {'product': 'Keyboard', 'category': 'tech', 'price': 200},
    {'product': 'Jacket', 'category': 'clothes', 'price': 300},
]

def func_reduce(acc, item):
    if item['category'] not in acc:
        acc = acc | {item['category']: item['price']}
        return acc
    
    elif item['category'] in acc:
        acc[item['category']] += item['price']
        return acc
    

test = reduce(
    func_reduce,
    sales,
    {}
)

print(test)