import random
eng = []
kor = []
score = 0
order = 0

for i in range(10):
    eng.append(input("단어를 입력하시오 : "))
    kor.append(input("뜻을 입력하세오 : "))

print("10개의 단어를 입력하셨습니다\n이제부터 단어시험을 시작합니다")

while len(eng) > 0:
    order = random.randint(0, len(eng) + 1)
    