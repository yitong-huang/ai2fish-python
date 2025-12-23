class BankAccount:
    def __init__(self, accountNumber, balance):
        self.__accountNumber = accountNumber
        self.__balance = float(balance)

    # Getter for balance
    def getBalance(self):
        return self.__balance

    # Setter for balance
    def setBalance(self, newBalance):
        self.__balance = newBalance

    # Getter for account number
    def getAccountNumber(self):
        return self.__accountNumber


class Deposit(BankAccount):
    def __init__(self, accountNumber, balance, deposit):
        super().__init__(accountNumber, balance)
        self.deposit = float(deposit)

    def myDeposit(self, amount):
        if amount > 0:
            new_balance = self.getBalance() + amount
            self.setBalance(new_balance)


class Withdraw(Deposit):
    overdraft_used = False  # class-level variable allowing only one overdraft/month

    def __init__(self, accountNumber, balance, amount):
        super().__init__(accountNumber, balance, deposit=0)
        self.amount = float(amount)

    def myWithdraw(self, amount):
        current_balance = self.getBalance()

        if amount > current_balance:
            print("Withdraw amount more than balance.")
            if Withdraw.overdraft_used:
                print("Overdraft already used this month. Cannot process another overdraft.")
                return current_balance

            ask = input("Do you need overdraft? enter (yes/no): ").strip().lower()

            if ask == "yes" or ask == "y":
                Withdraw.overdraft_used = True  # overdraft is now used
                new_balance = current_balance - amount
                self.setBalance(new_balance)

                print(f"Current balance after transaction: £{new_balance}")

                rate = float(input("Enter bank percent interest rate/charges: "))
                interest_rate = rate / 100
                interest_amount = abs(new_balance) * interest_rate

                new_balance_after_interest = new_balance - interest_amount
                self.setBalance(new_balance_after_interest)

                print(f"Current balance after '{rate}%' overdraft charges: £{new_balance_after_interest}")
                print(f"Bank monthly overdraft charges plus interest: £{abs(new_balance_after_interest - new_balance)}")

                return new_balance_after_interest

            else:
                print("Thank you for banking with us! See you again!!")
                return current_balance

        else:
            new_balance = current_balance - amount
            self.setBalance(new_balance)
            return new_balance


class Transaction(Withdraw):
    def __init__(self, accountNumber, balance, withdraw):
        super().__init__(accountNumber, balance, withdraw)
        self.withdraw = float(withdraw)

    # Set balance (mutator)
    def setTransactionBalance(self, newBalance):
        self.setBalance(newBalance)

    # Get balance (accessor)
    def getTransactionBalance(self):
        return self.getBalance()

    # Optional: return account number
    def getTransactionAccount(self):
        return self.getAccountNumber()


# ----------------------------------------------------------
# BankAccountTest Driver Class
# ----------------------------------------------------------
class BankAccountTest:
    @staticmethod
    def run():
        accNo = input("Enter account number: ")
        balance = float(input("Enter account balance: "))
        deposit = float(input("Enter deposit: "))
        withdraw = float(input("Enter amount to withdraw: "))

        print(f"Customer with account number: {accNo} has an initial bank account balance")
        print(f"of: £{balance}")

        # --- BankAccount Instance ---
        bank_acc = BankAccount(accNo, balance)

        # --- Deposit Instance ---
        dep = Deposit(accNo, balance, deposit)
        dep.myDeposit(deposit)
        print(f"Total balance after deposit: £{dep.getBalance()}")

        # --- Transaction (Withdraw + overdraft logic) ---
        trans = Transaction(accNo, dep.getBalance(), withdraw)
        final_balance = trans.myWithdraw(withdraw)

        print(f"Current balance after transaction: £{final_balance}")


# ----------------------------------------------------------
# Program Entry Point
# ----------------------------------------------------------
if __name__ == "__main__":
    BankAccountTest.run()
