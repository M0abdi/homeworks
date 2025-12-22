#Create a program that converts temperatures between Celsius and Fahrenheit




def temperature_converter():
    print("=== Temperature Converter ===")
    
    # Get input from user
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Enter unit (C or F): ").upper()
        
        # Validate unit input
        if unit not in ['C', 'F']:
            print("Error: Please enter 'C' for Celsius or 'F' for Fahrenheit")
            return
        
        # conversion
        if unit == 'C':
            converted_temp = (temp * 9/5) + 32
            print(f"{temp:.2f}°C = {converted_temp:.2f}°F")
        else:
            converted_temp = (temp - 32) * 5/9
            print(f"{temp:.2f}°F = {converted_temp:.2f}°C")
            
    except ValueError:
        print("Error: Please enter a valid number for temperature")

# Run
temperature_converter()
