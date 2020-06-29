#!/usr/bin/python3
round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1   
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer == "Brian":
        print("Correct!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry. Try again!")

