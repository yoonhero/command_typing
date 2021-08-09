from time import time
from words import getWords


def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors


def typingSpeed(iprompt, stime, etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time
    return speed


def timeElapsed(stime, etime):
    time = etime - stime

    return time


if __name__ == '__main__':

    prompt = getWords()
    print("Type this: '", prompt, "'")

    input("press ENTER when you are ready!")

    stime = time()
    iprompt = input()
    etime = time()

    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    print("총 걸린 시간: ", time, "s")
    print("자신의 평균 타이핑 속도 : ", speed, "words / minute")
    print("오타 : ", errors, "errors")
# 이거 좀 오류가 많은데 ㅋ.ㅋ 그게 아니라 속도 측정에 ㅋ.ㅋ 엄청 긎게 친게 더 빠르게 나옴
# 그래? 실행 해보니 아무 탈 없길래 ㅋ,ㅋ  아아아아 바ㅏㄴ대로 해야되ㅡㄴ데
