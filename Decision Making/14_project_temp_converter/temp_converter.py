# Project 2: Temperature Converter (Celsius to Fahrenheit)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    try:
        c_temp = float(input("Enter Temperature in Celsius: "))
        f_temp = celsius_to_fahrenheit(c_temp)
        print(f"Temperature in Fahrenheit: {f_temp:.1f}°F")
    except ValueError:
        print("Invalid input! Please enter a valid number for temperature.")
