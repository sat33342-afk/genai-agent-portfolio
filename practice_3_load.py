import json

claim = {"claim_id" : "c1", 
         "amount" : 75000,
         "claim_type" : "fire",
         "policyholder": 
         {"name" : "Mike",
         "address" : {"city" : "Boston"}
    }
}

with open ("claims.json", "w") as f:
    json.dump (claim, f)

def load_claims(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("file not found")

data = load_claims("claims.json")
print(data["claim_id"])
print(data["policyholder"] ["address"]["city"])
print(data)

load_claims("nothing.json")







