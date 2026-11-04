import json

claim1 = {"claim_id": "C1", "policyholder": {"name": "John", "address": {"city": "Ohio"}}}
claim2 = {"claim_id": "C2", "policyholder": {"name": "Ravi"}}
claim3 = {"claim_id": "C3"}

def get_city(claim):
    holder = claim.get("policyholder", {})
    address = holder.get ("address", {})
    city = address.get ("city", "unknown")
    return city

print (get_city (claim1))
print (get_city (claim2))
print (get_city (claim3))

