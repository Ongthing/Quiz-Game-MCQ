def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print("_______________________")
            print(i)
        guess = input("Enter (A, B, C, or D ): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
def check_answer(answer, guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0
def display_score(correct_guesses, guesses):
    print("______________")
    print("Results")
    print("_________________")
    print("Answer")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("guesses :", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("You score is :"+str(score)+"%")

def play_again():
    response = input("Do you play_again? (yes/no): ")
    response.upper()
    if response == "yes":
        return True
    else:
        return False
questions = {
    "Who created python?: ": "A",
    "What year was python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}
options = [["A. Guido van Rossum", "B. Elon musk", "C. Bil Gates", "D. Mark"],
           ["A. 1999", "B. 1991", "C. 2016", "D. 2000"],
           ["A. Lonly islan", "B. Smosh", "C. Monty python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth"]]
new_game()
while play_again():
    new_game()
print("byeeee ongthing")