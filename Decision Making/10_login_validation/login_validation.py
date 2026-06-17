# Login validation using logical operators (and, or, not)

def validate_login(username, password):
    correct_username = "admin"
    correct_password = "password123"
    
    if not username or not password:
        return "Login Failed: Username and password fields cannot be empty."
    
    if username == correct_username and password == correct_password:
        return "Login Successful! Welcome to your dashboard."
    else:
        return "Login Failed: Incorrect username or password."

if __name__ == "__main__":
    print("--- Login Validation ---")
    u_name = input("Enter Username: ").strip()
    p_word = input("Enter Password: ").strip()
    
    status_message = validate_login(u_name, p_word)
    print(status_message)
