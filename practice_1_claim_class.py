class Claim:
    def __init__(self,claim_id,amount,claim_type):
        self.claim_id=claim_id
        self.amount=amount
        self.claim_type=claim_type
        self.status="open"

    def summary(self):
        return self.claim_id + ": " + str(self.amount) + ", " + self.claim_type +  ", " + self.status
    
    def approve(self):
        self.status = "approved"

    def approve(self):
        if self.status == "rejected":
            print("Cannot approve a rejected claim")

        else:
            self.status = "approved"
    
    def reject(self, reason):
        self.status = "rejected"
        self.reason = reason


    