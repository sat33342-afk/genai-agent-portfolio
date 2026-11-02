import json

claim = {
    "claim_id": "C1",
    "amount": 75000,
    "claim_type": "fire",
    "policyholder": {
        "name": "John",
        "address": {"city": "Ohio"}
    }
}

claim2 = {
    "claim_id": "C2", "policyholder": {"name": "Ravi"}
}

def get_city(claim):
    holder = claim.get("policyholder", {})
    address = holder.get("address", {})  
    city  = address.get("city", "unknown")
    return city

with open("claims.json", "w") as f:
    json.dump(claim, f)

with open("claims.json", "r") as f:
    data = json.load(f)

print(data["claim_id"])
print(data["policyholder"]["address"]["city"])

print(get_city(claim))     
print(get_city(claim2))   
