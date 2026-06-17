# Project 3: Simple Login Validation

STORED_USERNAME = "admin"
STORED_PASSWORD = "1234"

def validate_login(username, password):
    if username == STORED_USERNAME and password == STORED_PASSWORD:
        return "Login Successful"
    else:
        return "Login Failed: Incorrect username or password."

if __name__ == "__main__":
    u_input = input("Username: ")
    p_input = input("Password: ")
    print()
    
    result = validate_login(u_input, p_input)
    print(result)
