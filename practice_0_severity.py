def check_claim_severity(claim_amount, claim_type):
    if claim_amount>50000:
        return "high"
    elif claim_amount>10000:
        return "medium"
    else:
        return "low"

#claim_amount = 75000
#claim_type = "fire"

claims = [(75000, "fire"), (25000, "water"), (5000, "auto"), (60000, "liability")]

pr#int (check_claim_severity(claim_amount,claim_type))

for claim in claims:
    print(check_claim_severity (claim[0], claim[1]))