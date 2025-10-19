def analyze_digits(digit_string):
    digit_count = {}

    for char in digit_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))

    top_three = sorted(sorted_digits[:3], key=lambda x: x[0])

    result_dict = dict(top_three)

    return result_dict


test_string = "123456789012343122567890123456789012343344"
print(f"Исходная строка: {test_string}")
result = analyze_digits(test_string)
print("Топ-3 самых частых чисел:", result)

print("Результат в порядке возрастания ключа:")
for digit, count in sorted(result.items()):
    print(f"Цифра {digit}: {count} раз(а)")