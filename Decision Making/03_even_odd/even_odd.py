# Check whether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    print("--- Even or Odd Checker ---")
    try:
        val = int(input("Enter an integer: "))
        result = check_even_odd(val)
        print(f"The number {val} is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
