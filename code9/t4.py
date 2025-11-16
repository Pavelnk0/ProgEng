import time


# Определяем класс декоратора
class LerinDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()  # Записываем время начала
        result = self.func(*args, **kwargs)
        end_time = time.time()  # Записываем время окончания
        execution_time = end_time - start_time  # Подсчитываем время выполнения
        print(f"Время выполнения функции '{self.func.__name__}': {execution_time} секунд")  # Выводим время выполнения
        return result

    # Используем LerinDecorator для функции факториала


@LerinDecorator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Используем LerinDecorator для функции генерации квадратов
@LerinDecorator
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]


# Основной блок выполнения
if __name__ == '__main__':
    print(factorial(17))  # Вычисляем и печатаем факториал числа 17
    print(generate_squares(17))  # Генерируем и печатаем квадраты чисел от 1 до 17