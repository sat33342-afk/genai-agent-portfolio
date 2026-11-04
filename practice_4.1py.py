claims = [
    {"id": "C1", "type": "fire", "amount": 75000},
    {"id": "C2", "type": "water", "amount": 25000},
    {"id": "C3", "type": "fire", "amount": 5000},
    {"id": "C4", "type": "auto", "amount": 12000},
]

new_claim = []

for claim in claims:
    if claim ["amount"] > 20000:
        new_claim.append(claim)

print (new_claim)


group = {}

for claim in claims:
    claim_type = claim ["type"]
    if claim_type not in group:
        group[claim_type] = []
    group[claim_type].append(claim ["id"])

print (group)


total = {}

for claim in claims:
    claim_type = claim ["type"]
    if claim_type not in total:
        total [claim_type] = 0
    total[claim_type] += claim["amount"]

print (total)
