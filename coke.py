print("Amount Due: 50")

def calculate_change(amount_paid):
    return amount_paid - 50

amount_paid = 0

while amount_paid <50:
    coin = int(input("Insert a coin (Accepted denominations: 1, 5, 10, 25, 50): "))
   
    if coin in[1, 5, 10, 15, 25, 50]:
        amount_paid += coin

        amount_due = 50 - amount_paid
        print("Amount due:", amount_due, "cents")

change = calculate_change(amount_paid)
print("Change: ", change, "cents")