class Category:
   
    # Constructor
    def __init__(self, category_name:str):
        self.name = category_name
        self.ledger = list()

    # Print object
    def __str__(self):
        asterisk = "*"
        num_of_asterisks = (30 - len(self.name)) // 2
        # Title line of 30 chars with centered name of category
        output = f"{asterisk * num_of_asterisks}{self.name}{asterisk * (30 - num_of_asterisks - len(self.name))}\n"
    
        # Total sum
        total = 0

        for item in self.ledger:
            total += item["amount"]
            desc = item["description"][:23]
            amnt = f"{item['amount']:.2f}".rjust(30 - len(desc))
            output += f"{desc}{amnt}\n"

        output += f"Total: {total:.2f}"
        return output
    
    # Deposit
    def deposit(self, amount:float, description=""):
        object_to_append = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(object_to_append)

    # Withdraw
    def withdraw(self, amount:float, description=""):
        isWithdrawPossible = self.check_funds(amount)
        if isWithdrawPossible:
            object_to_append = {
                "amount": -amount,
                "description": description
            }
            self.ledger.append(object_to_append)
        return isWithdrawPossible
    
    # Get balance
    def get_balance(self):
        current_balance = 0
        for transaction in self.ledger:
            current_balance += transaction["amount"]
        return current_balance

    # Transfer
    def transfer(self, amount:float, budget_category):
        isTransferPossible = self.check_funds(amount)
        if isTransferPossible:
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
        return isTransferPossible
    
    # Check funds
    def check_funds(self, amount:float):
        isThereSufficientFunds = self.get_balance() >= amount
        return isThereSufficientFunds
