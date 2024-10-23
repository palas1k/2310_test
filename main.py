# Напишите функцию, которая берет список неотрицательных целых чисел
# и строк и возвращает новый список с отфильтрованными числами.

def filter_non_negative_integers(source: list) -> list:
    return [x for x in source if isinstance(x, int)]


input_list = [1, '2', 3, 'hello', 4, 0, '1']
filtered_list = filter_non_negative_integers(input_list)
print(filtered_list)


# Напишите функцию accum:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(source: str) -> str:
    return '-'.join((i * int(x + 1)).capitalize() for x, i in enumerate(source))


print(accum("abcd"))
print(accum('RqaEzty'))
print(accum("cwAt"))

# Напишите функцию, которая выдаёт сумму выручку на основании входного формата данных
products = [
    {'name': 'Футболка', 'price': 20, 'quantity': 2},
    {'name': 'Джинсы', 'price': 50, 'quantity': 1},
    {'name': 'Носки', 'price': 5, 'quantity': 10},
    {'name': 'Штаны', 'price': 30, 'quantity': 1}
]


def count_revenue(products: dict) -> int:
    return sum(i['price'] * i['quantity'] for i in products)


print(count_revenue(products))
