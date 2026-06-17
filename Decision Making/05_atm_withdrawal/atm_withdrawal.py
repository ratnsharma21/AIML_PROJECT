# ATM withdrawal validation (Nested If)

def validate_withdrawal(balance, amount, daily_limit=20000):
    if amount > 0:
        if amount <= daily_limit:
            if amount <= balance:
                new_balance = balance - amount
                return True, f"Withdrawal successful! Please collect your cash.\nRemaining Balance: {new_balance}"
            else:
                return False, "Transaction Failed: Insufficient balance."
        else:
            return False, f"Transaction Failed: Amount exceeds daily limit of {daily_limit}."
    else:
        return False, "Transaction Failed: Amount must be greater than zero."

if __name__ == "__main__":
    print("--- ATM Withdrawal Validation ---")
    current_balance = 50000.0
    print(f"Your Account Balance: {current_balance}")
    print("Daily Limit: 20000")
    
    try:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        success, message = validate_withdrawal(current_balance, withdraw_amount)
        print(message)
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")
