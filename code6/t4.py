with open('banned_words.txt', 'r') as f:
    banned = f.read().split()

text = input("Введите текст: ")
text.lower()
result = text


for word in banned:
    result = result.replace(word, '*' * len(word))
    result = result.replace(word.upper(), '*' * len(word))
    result = result.replace(word.capitalize(), '*' * len(word))

print("Результат:")
print(result)