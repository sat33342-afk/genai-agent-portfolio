from pydantic import BaseModel, ValidationError, Field
from typing import Literal

class ClaimIntake(BaseModel):         #inheritance
    policy_number: str = Field(pattern=r"^POL-")
    amount: int = Field(gt=0)
    claim_type: Literal["fire", "water", "auto", "liability"]
    description : str = Field(min_length=10)


valid = {
    "policy_number": "POL-101",
    "amount": 75000,
    "claim_type": "fire",
    "description": "Kitchen fire damage to walls",
}

invalid_1 = {"policy_number": "ABC-5", "amount": 75000, "claim_type": "fire", "description": "Kitchen fire damage to walls"}
invalid_2 = {"policy_number": "POL-101", "amount": 0, "claim_type": "fire", "description": "Kitchen fire damage to walls"}
invalid_3 = {"policy_number": "POL-101", "amount": 75000, "claim_type": "flood", "description": "Kitchen fire damage to walls"}
invalid_4 = {"policy_number": "POL-101", "amount": 75000, "claim_type": "water", "description": "Kitchen"}


for data in [valid, invalid_1, invalid_2, invalid_3, invalid_4]:
    try:
        claim = ClaimIntake.model_validate(data)   #pydantic step
        print("OK:", claim)
    except ValidationError as e:
        print("Invalid:", e)

claim = ClaimIntake.model_validate(valid)