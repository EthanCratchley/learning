import random

MIN1_NUM = 0
MAX1_NUM = 10

MIN2_NUM = 20
MAX2_NUM = 40

MIN3_NUM = 40
MAX3_NUM = 80

level = []

def main():
    while True:
        get_level()
        generate_integer(level)
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

def get_level():
    global level
    level = int(input("Level 1-3: "))

def generate_integer(level):
    if level == 1:
        num_1 = random.randint(MIN1_NUM, MAX1_NUM)
        num_2 = random.randint(MIN1_NUM, MAX1_NUM)
        print("What is " + str(num_1) + " + " + str(num_2) + " ?")
        total = num_1 + num_2
    elif level == 2:
        num_3 = random.randint(MIN2_NUM, MAX2_NUM)
        num_4 = random.randint(MIN2_NUM, MAX2_NUM)
        print("What is " + str(num_3) + " + " + str(num_4) + " ?")
        total = num_3 + num_4
    elif level == 3:
        num_5 = random.randint(MIN3_NUM, MAX3_NUM)
        num_6 = random.randint(MIN3_NUM, MAX3_NUM)
        print("What is " + str(num_5) + " + " + str(num_6) + " ?")
        total = num_5 + num_6

    user_input = int(input("Your answer: "))

    if user_input == total: 
        print("Correct!")
    else:
        print("Incorrect. The correct answer is " + str(total))

if __name__ == "__main__":
    main()