import random

rcp = ["가위", "바위", "보"]
user = 0
computer = 0
result = 0

def result_show(who):
    if who == 1:
        return "우리 비겼네"
    elif who == 2:
        return "니가 이겼네"
    elif who == 3:
        return "니가 졌네"

user = input("가위 바위 보 하자: ")
computer = random.choice(rcp)

if user == computer:
    result = 1
elif user == "가위":
    if computer == "보":
        result = 2
    else:
        result = 3
elif user == "바위":
    if computer == "가위":
        result = 2
    else:
        result = 3
elif user == "보":
    if computer == "바위":
        result = 2
    else:
        result = 3
        
print(f"유져 : {user}, 컴퓨터: {computer}\n ===>>> {result_show(result)}")