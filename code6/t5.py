search_word = input("Введите слово для поиска: ")

with open('article.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
count = 0

for word in words:
    clean_word = word.strip('.,!?;:"()')
    if clean_word.lower() == search_word.lower():
        count += 1

print(f"Слово '{search_word}' встречается {count} раз")