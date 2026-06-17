# List Operations Functions using map, filter, and reduce

from functools import reduce

def demonstrate_list_operations():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original List: {numbers}")
    
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print(f"Doubled List (using map): {doubled_numbers}")
    
    even_numbers = list(map(int, filter(lambda x: x % 2 == 0, numbers)))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even Numbers (using filter): {even_numbers}")
    
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    print(f"Sum of List Elements (using reduce): {sum_of_numbers}")
    
    product_of_numbers = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
    print(f"Product of [1, 2, 3, 4, 5] (using reduce): {product_of_numbers}")

if __name__ == "__main__":
    print("--- List Operations (map, filter, reduce) ---")
    demonstrate_list_operations()
