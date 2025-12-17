class BankAccount:
    interest_rate = 0.02

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @classmethod
    def vchange_interest_tate(cls, new_rate):
        cls.interest_rate = new_rate
        print("Interes cambiado")

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                print("Retiro exitoso")
            else:
                print("Saldo insuficiente")
        else:
            print("Monto debe ser mayor a cero")


account1 = BankAccount("Andres", 1000)
account2 = BankAccount("Jpse", 300)

print(BankAccount.interest_rate)
BankAccount.vchange_interest_tate(0.3)
print(BankAccount.interest_rate)

account1.withdraw(500)
account2.withdraw(500)

print(BankAccount.validate_amount(500))