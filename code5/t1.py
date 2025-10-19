user_input = input("Введите числа через пробел: ")

numbers_list = user_input.split()

numbers_list = [int(num) for num in numbers_list]

numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)