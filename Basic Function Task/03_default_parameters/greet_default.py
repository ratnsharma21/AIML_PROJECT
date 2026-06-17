# Function with default parameters

def greet(name="Guest"):
    print(f"Welcome, {name}!")

if __name__ == "__main__":
    print("--- Function with Default Parameters ---")
    
    print("Calling greet() with no arguments:")
    greet()
    
    print("\nCalling greet() with argument 'John':")
    greet("John")
    
    print("\nCalling greet() with user input:")
    custom_name = input("Enter custom name (or press Enter for default): ").strip()
    if custom_name:
        greet(custom_name)
    else:
        greet()
