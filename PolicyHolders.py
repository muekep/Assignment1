class PolicyHolders:
    def __init__(self,Name,Contact_number,policyholder_id):
        self.Name=Name
        self.Contact_number=Contact_number
        self.status="Registered" # Default status upon creation
        self.policyholder_id=policyholder_id
        self.date_of_registration=None
    def register (self,date_of_registration): #Registering PolicyHolder
        self.status="Active"
        self.date_of_registration=date_of_registration
    def suspend(self): #suspending policy holder
        self.status="Suspended" 
    def reactivate(self):
        self.status="Active"
    def update_contact(self,new_contact):#Update contact details
        self.Contact_number=new_contact
    def __str__(self): #Return a string representation of the policyholder object
        return f"Policyholder ID:{self.policyholder_id}, Name:{self.Name},Status:{self.status}"
#Example 
Policyholder1 = PolicyHolders("Cosmas Mueke","+2547089765","FG5565")
Policyholder1.register("23/03/2025")
