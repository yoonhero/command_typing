from pyfiglet import figlet_format


def welcome():
    print(figlet_format('START!', font='starwars'))

    print("\nWelcome to Typing Text !!!!\n")
    print("You have to type a word that appear on the screen")
    print("\n-----------------------------\n")
    if input("start(s) or quit(q): ") == "s":
        return True
    else:
        return False


if __name__ == "__main__":
    welcome()
