from pydantic import BaseModel, ValidationError, Field

class ClaimIntake(BaseModel):         #inheritance
    claim_id: str
    amount: int = Field(gt=0)
    claim_type: str

good_data = {"claim_id": "C1", "amount": 75000, "claim_type": "fire"}
bad_data = {"claim_id": "C2", "amount": "lots", "claim_type": "water"}

for data in [good_data, bad_data]:
    try:
        claim = ClaimIntake.model_validate(data)   #pydantic step
        print("OK:", claim)
    except ValidationError:
        print("Invalid:", data)


claim = ClaimIntake.model_validate(good_data)

#Serialization
print(claim.model_dump())          # a Python dictionary
print(claim.model_dump_json())     # JSON text