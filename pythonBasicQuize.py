# create a quize console app
# Path: quize.py
print("Welcome to the quiz!")
print("Answer the following questions:")
def new_func():
    print("What is the capital of France?")
    answer = input()
    if answer.lower() == "paris":
        print("Correct!")
    else:
        print("Incorrect!")
    print("What is the capital of Spain?")
    answer = input()
    if answer.lower() == "madrid":
        print("Correct!")
    else:
        print("Incorrect!")
    print("What is the capital of Italy?")
    answer = input()
    if answer.lower() == "Rome":
        print("Correct!")
    else:
        print("Incorrect!")

new_func()