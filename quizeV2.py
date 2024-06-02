# create a dictionary of 10 quize questions and answer
quize = {
    "What is the capital of France?": "Paris",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of England?": "London",
    "What is the capital of Russia?": "Moscow",
    "What is the capital of China?": "Beijing",
    "What is the capital of Japan?": "Tokyo",
    "What is the capital of India?": "New Delhi",
    "What is the capital of Australia?": "Canberra"
}

# create a quize console app using quize dictionary
print("Welcome to the quiz!")
def play_quize(quize):
    print("Answer the following questions:")
    # quit if user types "exit" or 3 consequitive wrong answers
    wrong_answer = 0
    for question, answer in quize.items():
        print(question)
        user_answer = input()
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            wrong_answer += 1
            print("Incorrect!")
            if wrong_answer == 3:
                print("You have given 3 wrong answers. Exiting the quiz!")
                return
        if user_answer.lower() == "exit":
            print("Exiting the quiz!")
            return

play_quize(quize)
# play quize again 3 times
for i in range(3):
    print("Play again!")
    play_quize(quize)
print("Thank you for playing the quiz!")