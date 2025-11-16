import functools

# Базовый декоратор
def my_decorator(func):
    @functools.wraps(func)  # Сохраняем данные оригинальной функции
    def wrapper(*args, **kwargs):  # Вложенная функция
        print(f"Вызывается {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} завершен")
        return result
    return wrapper

# Функция 1
@my_decorator
def say_hello(name):
    """Приветствует пользователя."""
    print(f"Привет, {name}!")

# Функция 2
@my_decorator
def calculate_sum(a, b):
    """Вычисляет сумму двух чисел."""
    return a + b

# Тестирование функций
say_hello("Мир")
result = calculate_sum(5, 10)
print(result)