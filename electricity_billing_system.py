class ElectricityBillingSystem:
    def __init__(self, customer_name, units_consumed):
        self.customer_name = customer_name
        self.units_consumed = units_consumed
        self.unit_rate = 5.0  # Price per unit in currency
        self.tax_rate = 0.10  # 10% tax

    def calculate_bill(self):
        base_amount = self.units_consumed * self.unit_rate
        tax_amount = base_amount * self.tax_rate
        total_amount = base_amount + tax_amount
        return base_amount, tax_amount, total_amount

    def generate_bill(self):
        base_amount, tax_amount, total_amount = self.calculate_bill()
        bill_details = f"""
        ================================
                ELECTRICITY BILL
        ================================
        Customer Name: {self.customer_name}
        Units Consumed: {self.units_consumed} kWh
        Rate per Unit: {self.unit_rate} per kWh
        --------------------------------
        Base Amount: {base_amount:.2f} currency
        Tax (10%): {tax_amount:.2f} currency
        --------------------------------
        Total Amount: {total_amount:.2f} currency
        ================================
        """
        return bill_details

# Function to take user input and generate bill
def main():
    print("Welcome to the Electricity Billing System")
    customer_name = input("Enter Customer Name: ")
    try:
        units_consumed = float(input("Enter Units Consumed: "))
        if units_consumed < 0:
            raise ValueError("Units consumed cannot be negative.")
        
        bill = ElectricityBillingSystem(customer_name, units_consumed)
        print(bill.generate_bill())
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
