import random
import time
from numpy import add
from pyfiglet import figlet_format
from wel import welcome
from words import getWords
from rest import getRanking, addData
import pandas
from utils import clearCommand


def printYourScore(score):
    print("Now Your Score: ", score, "\n")


def areYouReady():
    input("press ENTER when you are ready!!!\n")


def finishGame(score):
    print("Your Score: ", str(score), "\n")

    username = input("What's Your Name? \n\n")

    while username == "":
        username = input("")

    addData(username, score)

    ranking = getRanking()
    clearCommand()
    df = pandas.DataFrame(ranking)
    blankIndex = [''] * len(df)
    df.index = blankIndex
    print(df[['rank', 'username', 'score']])


def typinggame():
    w, h = 50, 50

    clearCommand()

    # if input is (s) and condition = True
    condition = welcome()

    score = 0
    count = 0
    if condition:
        while count <= 5:
            count += 1
            clearCommand()

            printYourScore(score)

            areYouReady()

            word = getWords()

            start_typing = time.time()

            inputval = input(word+"\n\n")
            while inputval == "":
                inputval = input("")

            clearCommand()
            if inputval == word:
                end_typing = time.time()
                score += int(len(word) / (end_typing - start_typing) * 100)

            clearCommand()

        finishGame(score)


if __name__ == "__main__":
    typinggame()
