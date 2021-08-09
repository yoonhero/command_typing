import requests
import random


def getWords():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    words = response.content.splitlines()
    while True:
        random_word = random.choice(words).decode('utf-8')

        if len(random_word) > 6:
            return random_word


if __name__ == "__main__":
    print(getWords())

# 왜 자꾸 따라오세요 !!
# ㅋㅋㅋ 아니 너 클릭되어있음 그 참가자에
# 그런김에 어떻게 하는건지 설명좀 wel에
