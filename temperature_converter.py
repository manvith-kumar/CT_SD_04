# CT_SD_04 - Temperature Converter with Human Facts
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def get_human_facts(temp, scale):
    facts = []
    
    # Reference points for each scale
    references = {
        'C': [
            (-273.15, "Absolute Zero"),
            (-40, "Extremely Cold (Antarctica Winter)"),
            (0, "Water Freezes"),
            (20, "Room Temperature"),
            (37, "Human Body Temperature"),
            (100, "Water Boils"),
            (150, "Oven Baking Temperature")
        ],
        'F': [
            (-459.67, "Absolute Zero"),
            (-40, "Extremely Cold (Antarctica Winter)"),
            (32, "Water Freezes"),
            (68, "Room Temperature"),
            (98.6, "Human Body Temperature"),
            (212, "Water Boils"),
            (302, "Oven Baking Temperature")
        ],
        'K': [
            (0, "Absolute Zero"),
            (233.15, "Extremely Cold (Antarctica Winter)"),
            (273.15, "Water Freezes"),
            (293.15, "Room Temperature"),
            (310.15, "Human Body Temperature"),
            (373.15, "Water Boils"),
            (423.15, "Oven Baking Temperature")
        ]
    }
    
    # Find closest reference point
    closest = min(references[scale], key=lambda x: abs(x[0] - temp))
    facts.append(f"🌡️ This is close to: {closest[1]} ({closest[0]}{'°' + scale if scale != 'K' else ' K'})")
    
    # Special facts
    if scale == 'C' and 36 <= temp <= 38:
        facts.append("💊 Normal human body temperature is 37°C")
    elif scale == 'F' and 97 <= temp <= 99:
        facts.append("💊 Normal human body temperature is 98.6°F")
    elif scale == 'K' and 309 <= temp <= 311:
        facts.append("💊 Normal human body temperature is 310.15K")
        
    return facts

def main():
    print("=== Temperature Converter ===")
    
    conversions = {
        '1': {'name': 'Celsius to Fahrenheit', 'func': celsius_to_fahrenheit, 'input': 'C', 'output': 'F'},
        '2': {'name': 'Fahrenheit to Celsius', 'func': fahrenheit_to_celsius, 'input': 'F', 'output': 'C'},
        '3': {'name': 'Celsius to Kelvin', 'func': celsius_to_kelvin, 'input': 'C', 'output': 'K'},
        '4': {'name': 'Kelvin to Celsius', 'func': kelvin_to_celsius, 'input': 'K', 'output': 'C'},
        '5': {'name': 'Fahrenheit to Kelvin', 'func': fahrenheit_to_kelvin, 'input': 'F', 'output': 'K'},
        '6': {'name': 'Kelvin to Fahrenheit', 'func': kelvin_to_fahrenheit, 'input': 'K', 'output': 'F'}
    }

    while True:
        print("\nOptions:")
        for key, val in conversions.items():
            print(f"{key}. {val['name']}")
        print("7. Exit")
        
        choice = input("\nSelect conversion (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
            
        if choice in conversions:
            try:
                temp = float(input(f"Enter temperature in {conversions[choice]['input']}{'°' if conversions[choice]['input'] != 'K' else ' '}: "))
                result = conversions[choice]['func'](temp)
                print(f"\nResult: {temp}{'°' if conversions[choice]['input'] != 'K' else ' '}{conversions[choice]['input']} = {result:.2f}{'°' if conversions[choice]['output'] != 'K' else ' '}{conversions[choice]['output']}")
                
                # Display human facts about input temperature
                print("\n" + "\n".join(get_human_facts(temp, conversions[choice]['input'])))
                
            except ValueError:
                print("Invalid input! Please enter a number.")
        else:
            print("Invalid choice! Please select 1-7")

if __name__ == "__main__":
    main()