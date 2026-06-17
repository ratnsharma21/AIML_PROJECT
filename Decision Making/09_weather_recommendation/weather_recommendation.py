# Weather recommendation system (elif Statements)

def get_weather_recommendation(temp):
    if temp >= 35:
        return "It is extremely hot! Recommendation: Stay indoors, drink plenty of water, and wear light cotton clothing."
    elif temp >= 25:
        return "It is warm and pleasant. Recommendation: Perfect weather for outdoor activities. Wear comfortable casual wear."
    elif temp >= 15:
        return "It is cool. Recommendation: A light jacket, cardigan, or sweater would be comfortable."
    elif temp >= 0:
        return "It is cold. Recommendation: Wear heavy coats, gloves, and warm thermal wear."
    else:
        return "It is freezing! Recommendation: Stay inside if possible, turn on the heating, and wear thick winter layers."

if __name__ == "__main__":
    print("--- Weather Recommendation System ---")
    try:
        temp_input = float(input("Enter current temperature in Celsius (°C): "))
        suggestion = get_weather_recommendation(temp_input)
        print(suggestion)
    except ValueError:
        print("Invalid input! Please enter a numeric temperature value.")
