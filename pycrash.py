def make_car(manufacturer, model, **options):
    # Create a dictionary to store car information.
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }

    # Loop through the additional options and add them to the car_dict.
    for option, value in options.items():
        car_dict[option] = value

    # Return the completed car dictionary.
    return car_dict

# Call the function with additional options for the Tesla car.
my_tesla = make_car('tesla', 'model 3', color='black', electric=True)

# Print the resulting car dictionary.
print(my_tesla)

