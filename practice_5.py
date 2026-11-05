# Ask: “do I want items, or do I want a value for a name?”
# •	Items (letters, claims, ids): use [] and .append.
# •	A value for a name (count, total, list under a type): use {} and dict[key] = value.


# # Counting
# texts = "Bharath"

# count = {}

# for text in texts:
#     if text not in count:
#         count [text] = 1
#     else:
#         count [text] = count [text] + 1

# print (count)


#Repeated letters
texts = "Bharath"
repeated = set()
for letter in texts:
    if texts.count(letter) > 1:
        repeated.add(letter)
print(repeated)

# #Non Repeated letters
# texts = "Bharath"
# repeated = set()
# for letter in texts:
#     if texts.count(letter) == 1:
#         repeated.add(letter)
# print(repeated)




