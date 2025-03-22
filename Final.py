from PolicyHolders import PolicyHolders
from Payment import Payment
from Product import Product

Policyholder1 = PolicyHolders("Cosmas Mueke","+2547089765","FG5565")
Policyholder1.register("23/03/2025")
policyholder2 = PolicyHolders("Animalia Plante","+2546772829","DG654")
policyholder2.register("24/03/2025")
policyholder2.register("25/05/2025")
product1 = Product.create_product("P01","Medical","Outpatient services","Family Members",34000)
payment1 = Payment("PY001",Policyholder1.policyholder_id, 35000,"Mobile Transfer",product1.product_id,"14/05/2025",Policyholder1.Name,Policyholder1.Contact_number,"pending")
payment2 = Payment("PY001",Policyholder1.policyholder_id, 35000,"Mobile Transfer",product1.product_id,"14/05/2025",policyholder2.Name,policyholder2.Contact_number,"pending")
payment1.complete_payment("02/04/2025")
payment2.complete_payment("06/07/2025")

# Display policyholder account details
def display_account_details(policyholder,payments):
    """
    Displays the account details for a policyholder, including their payments.

    Args:
        policyholder (Policyholder): The Policyholder object.
        payments (list): A list of Payment objects associated with the policyholder.
    """
    print("Policyholder Details:")
    print(policyholder)
    print("\nPayment History:")
    if payments:
        for payment in payments:
            print(payment)
    else:
        print("No payment history found.")

# Get payments for each policyholder
payments_for_policyholder1 = [Payment for payment in [payment1, payment2] if payment.policyholder_id == Policyholder1.policyholder_id]
payments_for_policyholder2 = [Payment for payment in [payment1, payment2] if payment.policyholder_id == policyholder2.policyholder_id]

# Display account details
display_account_details(Policyholder1, payments_for_policyholder1)
print("\n")
display_account_details(policyholder2, payments_for_policyholder2)
