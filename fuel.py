def convert(fraction):
    x, y = map(int, fraction.split("/"))

    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("X and Y must be integers.")

    if x > y:
        raise ValueError("X cannot be greater than Y.")

    if y == 0:
        raise ZeroDivisionError("Y cannot be 0.")

    percentage = x / y * 100
    return int(percentage)


def gauge(percentage):
    
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage) + "%"
    
def main():

    try:   

        fraction = input("Fraction: X/Y:")

        percentage = convert(fraction)

        result = gauge(percentage)

        print(result)
          
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()