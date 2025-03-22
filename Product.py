class Product:
    def __init__(self,product_id,name,description,details_of_coverage,premiums,status="Active"):
        self.product_id=product_id
        self.description=description
        self.details_of_coverage=details_of_coverage
        self.premiums=premiums
        self.name=name
        self.status=status
    @classmethod
    def create_product(cls,product_id,name,description,details_of_coverage,premiums):
        return cls(product_id,name,description,details_of_coverage,premiums)
    def update_product(self, name=None,description=None, details_of_coverage=None,premiums=None):
        if name:
            self.name=name
        if description:
            self.description=description
        if details_of_coverage:
            self.details_of_coverage=details_of_coverage
        if premiums:
            self.premiums
    def suspend_product(self):
        self.status = "Suspended"
    def reactivate_product(self):
        self.status="Active"
    def update_premium(self,new_premium):
        self.premiums =new_premium
    def __str__(self):
        return f"Product ID:{self.prodcut_id},Name: {self.name},Status:{self.status}"
