with open('article.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
print(f"Всего слов: {len(words)}")

word_count = {}
for word in words:
    word = word.lower().strip('.,!?;')
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common = max(word_count, key=word_count.get)
print(f"Самое частое слово: '{most_common}' ({word_count[most_common]} раз)")