def main():
    # Loop to ask until given accepted input
    while True:
        # Try and Except to make sure not to run into Errors
        try:
            miles_or_km = input("Miles or Km: ") # Ask which Unit of Measurement
            how_far = float(input("Distance: ")) # Ask for the distance 
            what_time = float(input("Time (Minutes): ")) # Ask for time in minutes
        except (ValueError, NameError, TypeError, UnboundLocalError):
            print("Please enter a valid input.")
        # If a valid input then run code to setup pace formatting
        else:
            pace_unit = "Minutes Per " + miles_or_km  
            if miles_or_km.lower() == 'km':
                pace_unit = "Minutes Per Kilometer"
            elif miles_or_km.lower() == 'miles':
                pace_unit = "Minutes Per Mile"

            your_pace = what_time / how_far # Pace Calculation
            print(f"You ran at a pace of {your_pace:.2f} {pace_unit}") # Print pace 
            break # End Loop

# Run code
main()
