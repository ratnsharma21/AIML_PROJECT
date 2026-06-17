# Recursive Factorial Program

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

if __name__ == "__main__":
    print("--- Recursive Factorial Calculator ---")
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            result = recursive_factorial(num)
            print(f"Factorial of {num} (using recursion) is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
