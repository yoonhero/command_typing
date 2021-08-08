import random
import time
from pyfiglet import figlet_format
from wel import welcome
from words import getWords


def clearCommand():
    print('\x1b[2J', end='')


def typingtest():
    w, h = 50, 50

    words = getWords()

    clearCommand()

    # if input is (s) and condition = True
    condition = welcome()

    score = 0
    start = time.time()
    now = time.time()

    while condition:
        if now - start > 5:
            break
        now = time.time()
        clearCommand()
        index = int(random.random() * len(words))
        inputval = input(words[index]+"\n\n")
        clearCommand()
        if inputval == words[index]:
            score += 1
            print("You're Right")
            clearCommand()
        else:
            print("You're wrong")
            clearCommand()

    print("Score: \n\n", figlet_format(str(score), font="starwars"))


if __name__ == "__main__":
    typingtest()
