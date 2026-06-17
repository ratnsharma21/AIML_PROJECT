# Function returning a value

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("--- Function with Return Value ---")
    try:
        val1 = float(input("Enter first number: "))
        val2 = float(input("Enter second number: "))
        
        result = add(val1, val2)
        print(f"Result of addition: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
