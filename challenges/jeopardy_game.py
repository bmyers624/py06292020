#!/usr/bin/python3
"""
Jeopardy Game
"""

import requests

def main():
    # prompt for initials
    player = input("Type in your initials: ")
    rounds = input("How many rounds would you like to play? ")

    # make a request to http://jservice.io/api/random
    zresp = requests.get(f"http://jersvice.io/api/random?count={rounds}")

    # strip off JSON from the 200 response
    listofquestions = zresp.json()

    for jquestion in listofquestions:

        print(f"Alex Says: {jquestion['question']}")
        playeranswer = input("\tType your Answer --> ")

        if playeranswer.lower() == jquestion['answer'].lower():
            print(f"Alex Says: That's right, you add {jquestion['value']} to your score")
            playerscore = playerscore + jquestion['value']
        else:
            print(f"Alex Says: Oh, not quite right! The answer we were looking for was {jquestion['answer']}")

        print(jquestion['answer'])
        print(jquestion['value'])

    # after 10 rounds, show the player's score
    print(f"Alex Says: Okay! Let's see how you did. \nLooks like your score is {playerscore}")


    # highscore tracker
    with open("jeopardyhighscores.txt") as jhs:
        highscorelist = jhs.readlines()
    highscorelist.sort()
    
    for score in highscorelist:
        if playerscore > int(score.rstrip("\n")):
            print("Looks like a high score!")
            highscorelist.pop(score)
            highscorelist.append(str(playerscore))
            break
    with open("jeopardyhighscores.txt", "w") as jhs:
        for score in highscorelist:
            jhs.write(score.rstrip+"\n")


if __name__ == "__main__":
    main()
