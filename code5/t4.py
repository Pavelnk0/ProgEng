def find_office_entries(tuple_data, employee_id):
    if employee_id not in tuple_data:
        return ()

    indices = [i for i, x in enumerate(tuple_data) if x == employee_id]

    if len(indices) == 1:
        return tuple_data[indices[0]:]

    return tuple_data[indices[0]:indices[1] + 1]


test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

print("Результаты поиска сегментов:")
for i, (tpl, emp_id) in enumerate(test_cases, 1):
    result = find_office_entries(tpl, emp_id)
    print(f"Тест {i}: {result}")