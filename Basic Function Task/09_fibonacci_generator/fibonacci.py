# Fibonacci Series Generator (Iterative & Recursive)

def generate_fibonacci_iterative(limit):
    """Generates the Fibonacci sequence up to 'limit' elements iteratively."""
    if limit <= 0:
        return []
    elif limit == 1:
        return [0]
        
    sequence = [0, 1]
    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def fibonacci_recursive(n):
    """Returns the n-th Fibonacci number using recursion (0-indexed)."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    print("--- Fibonacci Series Generator ---")
    try:
        count = int(input("Enter number of terms to generate: "))
        if count <= 0:
            print("Please enter an integer greater than 0.")
        else:
            iter_seq = generate_fibonacci_iterative(count)
            print(f"\nFibonacci Series (Iterative): {iter_seq}")
            
            recur_seq = [fibonacci_recursive(i) for i in range(count)]
            print(f"Fibonacci Series (Recursive): {recur_seq}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
