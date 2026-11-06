text = "Bharath"

nrepeated = set ()

for letter in text:
    if text.count(letter)==1:
        nrepeated.add(letter)

print (nrepeated)
