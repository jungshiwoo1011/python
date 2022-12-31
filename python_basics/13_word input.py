import random
import os
import time
clear = lambda: os.system('cls')
mode = 0

def word_in():
    kor = open("kor.txt",  "a", encoding = "UTF-8")
    eng = open("eng.txt",  "a", encoding = "UTF-8")
    answer = 0
    in_eng = ""
    in_kor = ""

    while True:
        answer = input("입력은 a, 끝내기는 q를 누루시오")
        if answer == "q":
            break
        elif answer == "a":
            in_eng = input("영단어를 입력하시오 : ")
            kor.write(f"{in_kor}\n")
            in_kor = input("한글뜻을 입력하시오 : ")
            eng.write(f"{in_eng}\n")
        else:
            print("잡몹윕렵햅업")

    kor.close()
    eng.close()

def test():
    kor = open("kor.txt",  "r", encoding = "UTF-8")
    eng = open("eng.txt",  "r", encoding = "UTF-8")

    kor_words = []
    eng_words = []

    for r in kor.readlines():
        kor_words.append(r.strip())
    for s in kor.readlines():
        eng_words.append(s.strip())

    questlons = ""
    answers = ""
    for num in range (len(kor_words)):
        questlons = kor_words[num]
        clear()
        answers = input(f"{questlons} 뜻을 가지는 영어단어를 적으시오 : ")
        if questlons == answers:
            print("정답")
        else:
            print("이바보")
        time.sleep(1)
    kor.close()
    eng.close()


while True:
    mode = input("1-단어입력 / 2-단어입력 / 3-앱 종료/n => ")
    if mode == 3:
        break
    elif mode == 1:
        word_in()
    elif mode == 2:
        test()
    else:
        print("잘못 입력")
