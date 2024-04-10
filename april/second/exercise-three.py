x = {"Rom": "Rome",
     "Berlin": "Berlin",
     "Santo Domingo": "Santo Domingo",
     "Paris": "Paris",
     "London": "London",
     "Lagos": "Rome",
     "Washington D.C": "Washington D.C",
     "Wien": "Vienna",
     "Kopenhagen": "Copenhagen",
     "Prag": "Prague"}

print(x.keys())
x = dict(sorted(x.items()))
print(x)
for key in x.keys():
    print(x[key])