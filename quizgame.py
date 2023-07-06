# ------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------")
        print (key)
        for i in options[question_num-1]:
            print(i)
        guess = input ("Enter: (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
    
# ------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("Results")
    print("------------------------------")
    
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
        print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
        print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")
# ------------------------------
def play_again():
 
    response = input('Do you want to play again? (yes or no):').lower()

    if response == "yes":
        return True
    elif response == "no":
        return False
    else:
        print("Invalid Input. Please enter yes or no.")
        return play_again()
# ------------------------------

questions = {
"What is the most popular religion?: ": "A",
"Who won the last Superbowl?: ": "A",
"What is the most spoken lanuage?: ": "C",
"What is the biggest country in the world?: ": "A"
}

options = [["A. Christianity, B. Muslim, C. Islam, D. Budhist"],
["A. Chiefs, B. Bucs, C. Bills, D. Cowboys"],
["A. Spanish, B. English, C. Chinese, D. Japanese"],
["A. Russia, B. Canada, C. USA, D. China"]]

new_game()

while play_again():
    new_game()

print("Game Complete!")