import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except (requests.RequestException, KeyError, ValueError):
        print("Error: Failed to retrieve Bitcoin price.")
        sys.exit(1)

def calculate_cost(num_bitcoins):
    bitcoin_price = get_bitcoin_price()
    cost = num_bitcoins * bitcoin_price
    return cost

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    num_bitcoins_str = sys.argv[1]
    try:
        num_bitcoins = float(num_bitcoins_str)
    except ValueError:
        print("Error: Invalid number of bitcoins.")
        sys.exit(1)

    cost = calculate_cost(num_bitcoins)
    formatted_cost = "{:,.4f}".format(cost)

    print(f"The current cost of {num_bitcoins} Bitcoins in USD is: ${formatted_cost}")

if __name__ == "__main__":
    main()
