x = "„Die Sonne ist ein Stern und die Planten kreisen um die Sonne.“"
words = x.split(" ")
print(f"There are {len(words)} words in this string")

word_count = 0
for word in words:
    print(f'The word "{word}" occurs {words.count(word)} times in the string')

x = x.replace(".", "!")
print(f"replacing each dot with a exclamation mark yields us: {x}")

x = x.replace("und", "und ist ca. 4.6Mrd. Jahre alt")
print(f"this is our string if we append it: {x}")