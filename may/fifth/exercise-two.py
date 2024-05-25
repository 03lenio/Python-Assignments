with open("names.txt", "r+") as names_file:
    names = []
    for name in names_file.readlines():
        names.append(name)
    names.sort()
    for name in names:
        names_file.write(name)