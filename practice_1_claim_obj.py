from practice_1_claim_class import Claim

claim1 = Claim ("C1", 75000, "fire")
claim1.approve()

claim2 = Claim("C2", 25000, "water")
claim2.reject("missing documents")

claim2.approve()

print(claim2.summary())

print (claim1.summary())

#print(claim2.summary())
#print(claim2.reason)

#print (claim1.claim_id, claim1.amount, claim1.claim_type)
#print(claim1.status)
