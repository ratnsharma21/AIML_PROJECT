# Function with parameters and arguments

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    print("--- Function with Parameters ---")
    user_name = input("Enter your name: ").strip()
    if not user_name:
        user_name = "Muni"
    greet(user_name)
