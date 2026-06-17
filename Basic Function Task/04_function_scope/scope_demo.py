# Demonstration of variable scope (Local vs Global variables)

global_var = 100

def scope_demo_function():
    local_var = 50
    
    print("Inside function scope:")
    print(f"Accessing Global Variable (global_var): {global_var}")
    print(f"Accessing Local Variable (local_var): {local_var}")

if __name__ == "__main__":
    print("--- Scope Demonstration ---")
    scope_demo_function()
    
    print("\nOutside function scope:")
    print(f"Accessing Global Variable (global_var): {global_var}")
    
    print("Attempting to access local_var from global scope...")
    try:
        print(eval("local_var"))
    except NameError as e:
        print(f"NameError caught: {e}")
        print("Reason: Local variables defined inside a function are not accessible outside it.")
