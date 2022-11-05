drinks = {"콜라" : 2000, "환타" : 3000, "박카스" : 1500, "레드볼" : 4000, "칵테일" : 30000}
money = 0
customer = True
select = 0
choice = 0
income = 0

def display():
    print("*" * 22)
    print("*" * 5, "독약자판기", "*" * 5)
    print(drinks)
    print("*" * 22)
    print(f"잔액 : {money}")
    print("*" * 22)

while True:
    customer = True
    while customer:
        display()
        select = int(input("1. 돈넣기 / 2.물건사기 / 3.나가기 : "))

        if select == 1:
            money = int(input("금액입력 : "))
            continue
        elif select == 2:
            display()
            choice = input("음료선택 : ")
            if money >= drinks[choice]:
                print(f",{choice} 음료구매 완료 ")
                income += drinks[choice]
                money = money - drinks[choice]
            else:
                print("잔액부족")
                break
        elif select == 3:
            print("독약 자판기 이용 감사")
            if money > 0:
                print(f"환불금액 : {money}")
                money = 0
                customer = False
        elif select == 1470:
            print(f"오늘의 수입 : {income}")
            input("부좌 돼롸~ 수ㅖ꺄")
        else:
            print("잘못 눌렀다 새꺄")
