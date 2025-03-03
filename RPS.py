import random


print("Choices : rock, paper , scissor")
choices = ('rock','paper','scissor')
print("Make a Choice ")
while True:
    user_choice = input("ROCK /PAPER/ SCISSOR ? ")
    if user_choice not in choices:
        print('invalid choice')
        continue
    computer_choice = random.choice(choices)
    print("You chose : " + user_choice)
    print("Computer chose : " + computer_choice)

    if user_choice == computer_choice:
        print("Tie !!")
    elif (
            (user_choice == 'rock' and computer_choice == 'scissor') or
            (user_choice == 'scissor' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')):
        print("Congrats !!!!!!!  You Won!!")
    else:
        print("Computer Won!!")
    should_continue = input("Do you want to continue ? (y/n) :").lower()
    if should_continue == "n":
        break