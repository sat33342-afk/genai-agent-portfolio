text = "Bharath"
repeated = set()

for letter in text:
    if text.count (letter) > 1:
        repeated.add (letter)
print (repeated)