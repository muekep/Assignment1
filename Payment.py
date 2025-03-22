import datetime
from PolicyHolders import PolicyHolders
class Payment(PolicyHolders):
    def __init__(self,payment_id,policyholder_id, amount, payment_method, product_id,due_date,Name,Contact_number,status="pending"):
        super().__init__(Name,Contact_number,policyholder_id) #referencing the attributesof PolicyHoders class.
        self.payment_id=payment_id
        self.policyholder_id=policyholder_id
        self.product_id=product_id
        self.payment_date = None
        self.amount=amount
        self.due_date=due_date
        self.payment_method=payment_method
        self.status=status
        self.Penalty=0.0
    def complete_payment(self,payment_date):
        self.payment_date=payment_date
        self.status="Completed"
    def fail_payment(self):
        self.status="Failed"
    def send_reminder(self):
        print(f"Reminder: Dear {self.name}, Your Payment {self.payment_id} is due on {self.due_date}")
    def __str__(self):
        return f"Payment ID: {self.payment_id},Policyholder ID: {self.policyholder_id}, Amount:{self.amount}, Status: {self.status}"
    def apply_penalty(self,penalty_percentage):
        if self.status=="Overdue":
            self.penalty_applied = self.amount * penalty_percentage
            self.amount+=self.penalty_applied
            print(f"Penalty of {self.penalty_applied} applied to payments {self.payment_id}")
    def __str__(self):
        return f"Payment ID: {self.payment_id}, Policyholder ID:{self.policyholder_id}, Due Date: {self.due_date},Amount:{self.amount}, Status:{self.status}"
