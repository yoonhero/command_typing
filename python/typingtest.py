import random
import time
from pyfiglet import figlet_format

w, h = 50, 50

words = ["Apple", "Hello", "Computer", "NoteBook"]

print('\x1b[2J', end='')


def welcome():
    print(figlet_format('START!', font='starwars'))

    print("\nWelcome to Typing Text !!!!\n")
    print("You have to type a word that appear on the screen")
    print("\n-----------------------------\n")
    if input("start(s) or quit(q): ") == "s":
        return True
    else:
        return False


condition = welcome()
score = 0
start = time.time()
now = time.time()

while condition:
    if now - start > 5:
        break
    now = time.time()
    # for i in range(3):
    #   print(figlet_format('%s' % (3-i), font='starwars'))
    #   time.sleep(1)
    #   print('\x1b[2J', end='')
    print('\x1b[2J', end='')
    index = int(random.random() * len(words))
    inputval = input(words[index]+"\n\n")
    print('\x1b[2J', end='')
    if inputval == words[index]:
        score += 1
        print("You're Right")
        print('\x1b[2J', end='')
    else:
        print("You're wrong")
        print('\x1b[2J', end='')


print("Score: \n\n", figlet_format(str(score), font="starwars"))
