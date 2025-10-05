from datetime import datetime  # Импорт класса datetime из модуля datetime для работы со временем
from math import sqrt         # Импорт функции sqrt из модуля math для вычисления квадратного корня

def main(**kwargs):
    for key in kwargs.items():  # Перебор всех переданных аргументов
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)  # Вычисление длины вектора по формуле sqrt(x² + y²)
        print(result)  # Вывод результата

if __name__ == '__main__':
    start_time = datetime.now()  # Запись времени начала выполнения программы
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )  # Вызов функции main с передачей списков координат
    time_costs = datetime.now() - start_time  # Вычисление времени выполнения
    print(f"Время выполнения программы - {time_costs}")  # Вывод времени выполнения