text = input("Введите строку: ")
words = text.lower().split()
unique_words = set(words)

for word in unique_words:
    print(f"{word}: {words.count(word)}")