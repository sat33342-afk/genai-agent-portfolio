# PATTERN 1: write and read a text file
with open("claims.txt", "w") as f:
    f.write("C1: 75000, fire, open")

with open("claims.txt", "r") as f:
    text = f.read()
print(text)
# Note: "w" creates the file, "r" crashes if it is missing


# PATTERN 2: try/except around a file read
try:
    with open("nothing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")
# Note: name the error (FileNotFoundError), don't use a bare except


# PATTERN 3: safe nested lookup with .get
def get_city(claim):
    holder = claim.get("policyholder", {})
    address = holder.get("address", {})
    city = address.get("city", "unknown")
    return city

claim1 = {"claim_id": "C1", "policyholder": {"name": "John", "address": {"city": "Ohio"}}}
claim2 = {"claim_id": "C2", "policyholder": {"name": "Ravi"}}
print(get_city(claim1))
print(get_city(claim2))
# Note: each .get opens one drawer, and the default is used if it is missing


# PATTERN 4: a class with __init__, __str__ and a method
class Claim:
    def __init__(self, claim_id: str, amount: int, claim_type: str):
        self.claim_id = claim_id
        self.amount = amount
        self.claim_type = claim_type
        self.status = "open"

    def __str__(self):
        return self.claim_id + ": " + str(self.amount) + ", " + self.claim_type + ", " + self.status

    def approve(self):
        self.status = "approved"

c = Claim("C1", 75000, "fire")
print(c)
c.approve()
print(c)
# Note: self.x stores data on the object, and methods use or change it