class Policy:
    def __init__(self, policy_number:str, premium:int, policy_type:str):
        self.policy_number = policy_number
        self.premium = premium
        self.policy_type = policy_type

    def __str__(self):
        return self.policy_number + ": " + self.policy_type + ", " + "premium " + str (self.premium)


def check_premium_category(premium: int) -> str:
    if premium > 20000:
        return "premium tier"
    elif premium > 8000:
        return "standard tier"
    else:
        return "basic tier"

policy1 = Policy("POL-101", 5000, "auto")
print (policy1)
print(check_premium_category(policy1.premium))

    