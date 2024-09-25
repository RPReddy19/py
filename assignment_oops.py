"""
1. Create a Bank class which demonstrates the class, instance variables
and also the instance, class and static methods
"""

class Bank:
    # Class variable (shared across all instances)
    bank_name = "ABC National Bank"

    def __init__(self, name, balance):
        # Instance variables (unique to each instance)
        self.name = name
        self.balance = balance

    # Instance method (operates on instance data)
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. New balance is {self.balance}"

    # Instance method (operates on instance data)
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"{amount} withdrawn. New balance is {self.balance}"

    # Class method (operates on class data, accessed via the class itself)
    @classmethod
    def get_bank_name(cls):
        return f"Bank name: {cls.bank_name}"

    # Static method (does not operate on class or instance data, more like utility methods)
    @staticmethod
    def bank_rules():
        return "Banking hours: 9 AM - 5 PM, Monday to Friday"

# Example usage
account = Bank("John", 500)
print(account.deposit(300))         # Deposit operation using instance method
print(account.withdraw(100))        # Withdraw operation using instance method
print(Bank.get_bank_name())         # Access class method
print(Bank.bank_rules())            # Access static method


"""
2. Create a Vehicle class as Parent and choose any Vehicle (example: car) as Child class,
which should demonstrates the single inheritance
"""

The Toyota Corolla is starting.
The Toyota Corolla with 4 doors is driving.
The Toyota Corolla is stopping.


