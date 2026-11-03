claims = [
    {"id": "C1", "type": "fire", "amount": 75000},
    {"id": "C2", "type": "water", "amount": 25000},
    {"id": "C3", "type": "fire", "amount": 5000},
    {"id": "C4", "type": "auto", "amount": 12000},
]
# Pick out only the claims where the amount is above 20000.
#----------------------------------------------------------
# new_claim = []

# for claim in claims:
#     if claim ["amount"] > 20000:
#         new_claim.append(claim)

# print (new_claim)


#For each claim type, list the ids of the claims of that type.
#------------------------------------------------------------
# group = {}
# for claim in claims:
#     type = claim ["type"]
#     if type not in group:
#         group[type] = []
#     group[type].append(claim["id"])

# print(group)


#For each claim type, add up the amounts.
#----------------------------------------
total = {}

for claim in claims:
    type = claim ["type"]
    if type not in total:
        total[type] = 0
    total[type] += claim["amount"]

print(total)

