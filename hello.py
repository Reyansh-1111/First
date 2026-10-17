# Simple conversation and some games

print("Hey, nice to meet you! What is your name?")
name = input("Type your name: ").strip()
print(name, "That is a REALLY nice name")

print("How old are you?")
age = input("Type your age: ").strip()
print(age, "Am I right?")
answer = input("Type yes or no: ").strip().lower()

if answer == "yes":
    print("Yay, I got it right!!")
elif answer == "no":
    print("My bad!")
else:
    print("Please type yes or no.")

input()

print("I am really bored. Hey, I have an idea, let's do some art!!")
print("What is your favourite colour? Let's start our art with that only.")
colour = input("Type your favourite colour: ").strip()
print(colour, "Good pick!")

input()

print("AHHHHHHHHHHHHHHHHHHH, I am so EXHAUSTED")
print("Let's talk about something else")

print("Hey, I have a fun idea: let's play a game of would you rather!!")

input()

print("FIRST QUESTION")

while True:
    first = input("WOULD YOU RATHER: Be able to fly or be invisible? Type fly or invisible: ").strip().lower()

    if first == "fly":
        print("Flying would be amazing!")
        break
    elif first == "invisible":
        print("Interesting choice!")
        break
    else:
        print("Please choose fly or invisible.")

input()

print("SECOND QUESTION")

while True:
    second = input(
        "WOULD YOU RATHER: Read minds or control time? "
        "Type 'read minds' or 'control time': "
    ).strip().lower()

    if second == "read minds":
        print("Reading minds would be fascinating!")
        break
    elif second == "control time":
        print("Controlling time would be incredible!")
        break
    else:
        print("Please choose read minds or control time.")

input()

print("THIRD QUESTION")
print("Hey, I really forgot to ask the most basic questions yet")

while True:
    third = input("WOULD YOU RATHER: Be a boy or be a girl? Type your answer: ").strip().lower()
    if third == "boy":
        print("Being a boy would be great!")
        break
    elif third == "girl":
        print("Being a girl would be awesome!")
        break
    else:
        print("Please choose boy or girl.")

print("That was fun!!")
input()
print("I am sleepy, so just one last game before I go to sleep")
input()
print("Hey, how about a quiz?")
input()
print("Don't worry, it will be easy and short")
input()
print("Okay, let's start the quiz")

score = 0

print("FIRST QUESTION")
quiz_first = input("How many continents are there in the world?: ").strip()
if quiz_first == "7":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 7.")
print(f"Your score is {score}")
input()

print("SECOND QUESTION")
quiz_second = input("What is the largest ocean in the world?: ").strip().lower()
if quiz_second == "pacific ocean":
    print("Correct! Wow! You are on a roll!")
    score += 1
else:
    print("Incorrect! The correct answer is the Pacific Ocean.")
print(f"Your score is {score}")
input()

print("THIRD QUESTION")
quiz_third = input("What is the name of our galaxy?: ").strip().lower()
if quiz_third == "milky way":
    print("Correct! You are really smart!")
    score += 1
else:
    print("Incorrect! The correct answer is the Milky Way.")
print(f"Your score is {score}")
input()

print("FOURTH QUESTION")
quiz_fourth = input("What is 220 times 9?: ").strip()
if quiz_fourth == "1980":
    print("Correct! WOW!! You are really good at math!")
    score += 1
else:
    print("Incorrect! The correct answer is 1980.")
print(f"Your score is {score}")
input()

print("FIFTH QUESTION")
quiz_fifth = input("What is the capital of France?: ").strip().lower()
if quiz_fifth == "paris":
    print("Correct! You are really smart!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")
print(f"Your score is {score}")
input()

print("SIXTH QUESTION")
quiz_sixth = input("What is the largest planet in our solar system?: ").strip().lower()
if quiz_sixth == "jupiter":
    print("Correct! You are really smart!")
    score += 1
else:
    print("Incorrect! The correct answer is Jupiter.")
print(f"Your score is {score}")
input()

print(f"Final score: {score}/6")
print("AHHHH man, it was fun but I am really sleepy now, so I will have to go now!!")
input()
print("I will see you next time!!")
input()
print("I hope you had fun playing with me!!")
input()
print("Bye!!")
print(name, ", Bye!!")
input()
print("THANK YOU FOR PLAYING!!")
input()
