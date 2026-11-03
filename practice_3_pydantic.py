from pydantic import BaseModel

class ClaimIntake(BaseModel):         #inheritance
    claim_id: str
    amount: int
    claim_type: str

claim = ClaimIntake(claim_id="C1", amount=75000, claim_type="fire")
print(claim)
print(claim.model_dump())

#bad = ClaimIntake(claim_id="C2", amount="lots", claim_type="water")