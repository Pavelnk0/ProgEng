def remove_first_occurrence(tuple_data, element):
    temp_list = list(tuple_data)
    if element in temp_list:
        temp_list.remove(element)
    return tuple(temp_list)

test_cases = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

print("Результаты удаления элементов из кортежей:")
for i, (tpl, elem) in enumerate(test_cases, 1):
    result = remove_first_occurrence(tpl, elem)
    print(f"Тест {i}: {result}")