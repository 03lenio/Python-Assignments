x = []
for i in range(100):
    list_to_append = []
    for j in range(i):
        list_to_append.append(j)
    x.append(list_to_append)

print(x)

cleaned_x = []
for list_entry in x:
    for entry in list_entry:
        cleaned_x.append(entry)

print(cleaned_x)