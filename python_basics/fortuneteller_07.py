import random

def future():

    outfit = ["키 큰", "ㄱ같은", "우리 남자 코딩선생님 같은", "마동석"]
    gender = ["남자, 여자"]
    age = 0
    name = 0

    name = input("니 누구니?: ")

    print(f"{name}니 미래 와이프에 대해 말해준다")


    print(f"니 와이프는 {random.choic(outfit)} {random.choic(gender)} 요렇게 생겼다이. 나이는 마! {random.rndint(19, 99)}살이다 임마")