with open("claims.txt", "w") as f:
    f.write("C1: 75000, fire, open")

try:
    with open("claims.txt", "r") as f:
        text = f.read()
    print(text)

except:
    print ("File not found")