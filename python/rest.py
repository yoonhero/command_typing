import requests


def getRanking():
    response = requests.get("http://localhost:3000/ranking")
    return response.json()


def addData(username, score):
    response = requests.post(
        'http://localhost:3000/addData', data={"username": username, "score": score})
    response = response.json()
    if response["ok"]:
        return True
    return False


def seeProfile(username):
    response = requests.get("http://localhost:3000/user/"+username)
    return response.json()


if __name__ == "__main__":
    getRanking()
