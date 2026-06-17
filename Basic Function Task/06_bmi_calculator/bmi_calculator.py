# BMI Calculator Function

def calculate_bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
        
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
        
    return bmi, category

if __name__ == "__main__":
    print("--- BMI Calculator ---")
    try:
        weight = float(input("Enter weight in kg: "))
        height_cm = float(input("Enter height in cm: "))
        
        height_m = height_cm / 100
        
        bmi_value, bmi_category = calculate_bmi(weight, height_m)
        print(f"\nBMI Value: {bmi_value:.2f}")
        print(f"Category: {bmi_category}")
    except ValueError as e:
        print(f"Error: {e}. Please check your input.")
