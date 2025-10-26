with open('expenses.txt', 'a', encoding='utf-8') as f:
    category = input("Категория: ")
    amount = input("Сумма: ")
    f.write(f"{category} - {amount} руб.\n")
    print("Расход сохранен!")

print("\nВсе расходы:")
with open('expenses.txt', 'r', encoding='utf-8') as f:
    print(f.read())