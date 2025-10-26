with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

letters = 0
words = 0

for line in lines:
    for char in line:
        if char.isalpha():
            letters += 1
    words += len(line.split())

print(f"Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{len(lines)} lines")