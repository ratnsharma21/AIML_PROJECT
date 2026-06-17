# Traffic signal simulation (elif Statements)

def traffic_signal_action(color):
    color = color.strip().lower()
    
    if color == "red":
        return "STOP! The light is Red."
    elif color == "yellow":
        return "SLOW DOWN! The light is Yellow. Prepare to stop."
    elif color == "green":
        return "GO! The light is Green. Safe journey."
    else:
        return "Invalid Color! Traffic lights can only be Red, Yellow, or Green."

if __name__ == "__main__":
    print("--- Traffic Signal Simulation ---")
    light_color = input("Enter traffic light color (Red/Yellow/Green): ")
    action = traffic_signal_action(light_color)
    print(action)
