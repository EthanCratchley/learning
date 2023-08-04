def main():
    # Loop to ask until given accepted input
    while True:
        try:
            which_one = input("Are you converting from Celsius or Fahrenheit?: ").lower() # Are they converting from Celsius or Fahrenheit

            if which_one == "celsius": # Run this code if they chose Celsius to convert it
                c_input = float(input("Celsius: "))
                print(f"Fahrenheit: {(c_input * 1.8) + 32}")
                # Celsius to Fahrenheit Formula: (°C * 1.8) + 32 = °F

            elif which_one == "fahrenheit": # Run this code if they chose Fahrenheit to convert it
                f_input = float(input("Fahrenheit: "))
                print(f"Celsius: {(f_input - 32) / 1.8}")
                # Fahrenheit to Celsius Formula: (°F - 32) / 1.8 = °C

            else: 
                print("Please Enter a Valid Input.")
                continue

        except (ValueError, NameError, TypeError, UnboundLocalError): #Check for Errors
            print("Please enter a valid input.")
            continue

        break

# Run Code
main()
