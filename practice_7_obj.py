from practice_7_class import Claim

claim1 = Claim("C1", 75000, "fire")
claim2 = Claim("C2", 25000, "water")

claim2.reject("missing documents")
claim1.approve()
claim2.approve()

print (claim1)
print (claim2)


