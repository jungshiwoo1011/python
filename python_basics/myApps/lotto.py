import random


def lotto():

    lotto_numbers = []
    pisk = 0
    lotto_picks = []

    for i in range(45):
        lotto_numbers.append(i + 1)

    for j in range(7):
        pick = lotto_numbers.pop (random.randint(0, len(lotto_numbers) - 1))
        lotto_picks.append(pick)


    print(f"이번 주 1등 당첨 예상번호는 {lotto_picks} 입니다. 행운을 빕니다.")