# Project 4: Calculate Factorial Using Functions (Iterative)

def calculate_factorial(n):
    if n < 0:
        return None
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter Number: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            fact = calculate_factorial(num)
            print(f"Factorial: {fact}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
