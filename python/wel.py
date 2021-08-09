from pyfiglet import figlet_format
from rest import seeProfile
from utils import clearCommand
import pandas


def welcome():
    print(figlet_format('START!', font='starwars'))

    print("\nWelcome to Destoyed Typing TEXT War !!!!")
    print("\nThis is a Typing game! \n")
    print("You have to type a word that appear on the screen")
    print("\n-----------------------------")
    print("\nDo you want to start the game? \n")
    user_input = input(
        "if you want to start then press (s) \nor you want to see your profile (p)\nor you won't play the game then press (x): ")
    if user_input == "s":
        return True
    elif user_input == "p":
        clearCommand()
        username = input("What's your username?: ")
        profile = seeProfile(username)
        clearCommand()
        df = pandas.DataFrame(profile["user"]["games"])
        blankIndex = [''] * len(df)
        df.index = blankIndex
        print(df[["id", "score"]])
        return False
    else:
        return False


if __name__ == "__main__":
    welcome()

# 나 이제 뭐해?
# 뭘했는데?
# 이거 설명 추가하라며? ㅇㅇ
# 그래서 이거 더 쓸거 없는거 같아서 이제 뭐 하면 되냐고 물어본건데
# 그럼 저기 typingtest.py 가서 점수 추가를 초에 비례해서 추가하는 알고리즘을 만들어봐
# ㅇㅋㅇㅋ
# 이건 이제 그냥 실행할때 저 welcome 함수를 실행하는거고
# 다른 파일에서 실행할때는 무시하는거고
# 너가 파일 마음대로 돌아다니면서 고치면 됨
# 저기 왼쪽 위 오른쪽에 파일 아이콘 누르고
# python 폴더 누르고 들어가서 그 안에 .py 파일을 수정하셈
# 그니까 그걸 모르겠다고ㅜㅜㅜㅜㅜ!!!! 아아 ㅇㅋ 찾음 ㄱㅅㄱㅅ
# 그 설명 말고 라이브쉐어 어케쓰냐거

# 드디어 워디안을 끝냈다 ㅋ.ㅋ 이제 멸망 코딩 간다
# 저기 지금 다들 뭐하시나요???
# ㅡㅡ 왜? 아니 뭘했길래...
# 저 망했음요 발톱 빠질 거 같음 몰라 걍 구멍이 작게 생김
# 뭐하고 계신지? 저요? 네

# 네네넨네네ㅔㄴ네ㅔㄴ네넨네네넨네네넨네네ㅔㄴ네ㅔ넨넨네네네네넨네멀망럼니ㅏ얼미;아러;민아러;
# 멸망의 채팅창이네요
# 네네 싸우지 마세요
# 저요 피파 지금 중요한데요 ㅋㅋㅋ 지금 선수 뽑을라카는데 리그 결정 중입니다 아 그리고 시간 재는거까지 만들었음요 이제 오타 만들게요
# 안싸웠어 ??????
# 저 방금왔는데 뭐해요
# 아니 나 이거 사용법도 모른다고
# 다 니 잘못이야 ㅋㅋㅋ
 # 왜 내잘못이야 억울해ㅠㅠ
 # 내가 알려달랬는데 읽씹했잖아 ㅋㅋㅋ
# 알려# 암 ㄹ어그냥 어 하면 됨뭐됨해ㅋㅋㅋㅋㅋ 3명이서 하니깐 난리도 아니다 ㅋㅋㅋ뭥ㄹ민여ㅐ류민어류미낭ㄹ
#
# 3
##
# 끄아ㅏ아ㅏ아아아ㅏ아ㅏ아ㅏ앙
#
# 분데스리그 ㄱㄱ
# 리그 추천 좀요 21 tots 200 토큰 모아서 분데스 리가 ㅇㅋㅇㅋ 근데 라리가는 어떰?
# 라리가는 메시만 비싸서 ㅋ.ㅋ 아 분대스 리그에서 아는 사람이 ㅂ없어서 -> 홀란드 산없어서또...  자 갑니다 ㅋ갑니다샀다 과옂ㄴ
# 아니#아니 아#아아ㅏ닝나인아니아니아니아닝니아닝니ㅏ인니ㅏㅇ니나ㅣ니휸이ㅏㅓㅠ니류ㅣ 왜 왜왜왜오애 gk가 나오냐고고ㅗ고 ㅊㅋ
# 피알못 코알못은 다 당신 잘못입니다 :ㅒ 둘이 또 싸우네 안싸웠어
# 그래서 뭐 어떡하라구요
# 여기를 꾸며보세요 저는 워디안하러 ㅂㅂ 아 그래도 가치가 ㅋㅋㅋ
# 제가! 도움을! 요청했는데! 무시했잖ㅇㅁ
# 아니 잠시만 이거 완성된거임?
# ㄴㄴ 걍 대충 만들어놈
# ㅇㅋ

# 아니 딱히 고칠게 없어....
# 그럼 더 설명을 길게 써주세요 :ㅇㅋㅇㅋ
# 끼야호호ㅗㅎㅎ
# ?
# 그냥 타이핑 게임이라고 할게?
