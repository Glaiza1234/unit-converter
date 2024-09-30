def length_conversion(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meter = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    # Convert to meters, then to desired unit
    meters = value * to_meter[from_unit]
    return meters / to_meter[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "F" and to_unit == "K":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit, no conversion needed

def mass_conversion(value, from_unit, to_unit):
    # Conversion factors to grams
    to_gram = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592
    }
    # Convert to grams, then to desired unit
    grams = value * to_gram[from_unit]
    return grams / to_gram[to_unit]

def unit_converter():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Temperature")
        print("3. Mass")
        print("4. Exit")
        
        choice = input("Choose conversion type (1/2/3/4): ")
        
        if choice == '4':
            print("Thank you for using the unit converter. Goodbye!")
            break
        
        value = float(input("Enter the value to convert: "))
        
        if choice == '1':
            print("Available units: mm, cm, m, km, in, ft, yd, mi")
            from_unit = input("Enter the unit to convert from: ")
            to_unit = input("Enter the unit to convert to: ")
            result = length_conversion(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        
        elif choice == '2':
            print("Available units: C (Celsius), F (Fahrenheit), K (Kelvin)")
            from_unit = input("Enter the unit to convert from: ")
            to_unit = input("Enter the unit to convert to: ")
            result = temperature_conversion(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        
        elif choice == '3':
            print("Available units: mg, g, kg, oz, lb")
            from_unit = input("Enter the unit to convert from: ")
            to_unit = input("Enter the unit to convert to: ")
            result = mass_conversion(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    unit_converter()
