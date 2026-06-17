# Prime Number Checker Function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("--- Prime Number Checker ---")
    try:
        num = int(input("Enter an integer to check: "))
        if is_prime(num):
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is NOT a Prime Number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
